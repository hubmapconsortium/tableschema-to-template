from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from yattag import indent
import pytest
from yaml import safe_load

from create_xlsx import create_xlsx


@pytest.fixture(scope="module")
def xlsx_path():
    schema_path = Path(__file__).parent / 'fixtures/schema.yaml'
    schema = safe_load(schema_path.read_text())
    with TemporaryDirectory() as temp_dir_name:
        xlsx_path = Path(temp_dir_name) / 'template.xlsx'
        create_xlsx(schema, xlsx_path)
        yield xlsx_path


def assert_matches_fixture(xlsx_path, zip_path):
    # zipfile.Path is introduced in Python3.8, and could make this cleaner:
    # xml_string = zipfile.Path(xlsx_path, zip_path).read_text()
    with ZipFile(xlsx_path) as zip_handle:
        with zip_handle.open(zip_path) as file_handle:
            xml_string = file_handle.read().decode('utf-8')

    # Before Python3.8, attribute order is not stable in minidom,
    # so we need to use an outside library.
    pretty_xml = indent(xml_string)
    pretty_xml_fixture_path = (
        Path(__file__).parent / 'fixtures/output-unzipped' / zip_path
    )

    pretty_xml_tmp_path = Path('/tmp') / Path(zip_path).name
    pretty_xml_tmp_path.write_text(pretty_xml)

    assert pretty_xml.strip() == \
        pretty_xml_fixture_path.read_text().strip(), \
        'Update fixture?  ' + \
        f'cp {pretty_xml_tmp_path} {pretty_xml_fixture_path}'


@pytest.mark.parametrize(
    "zip_path",
    # TODO: Scan the directory for fixtures, instead of listing here.
    ['xl/worksheets/sheet1.xml',
     'xl/sharedStrings.xml',
     'xl/comments1.xml']
)
def test_create_xlsx(xlsx_path, zip_path):
    assert_matches_fixture(xlsx_path, zip_path)
