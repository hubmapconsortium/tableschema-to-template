from pathlib import Path
from tempfile import TemporaryDirectory
import zipfile
import xml.dom.minidom

from yaml import safe_load

from create_xlsx import create_xlsx


def assert_xmls_match(xlsx_path, zip_path):
    xml_path = zipfile.Path(xlsx_path, zip_path)
    dom = xml.dom.minidom.parseString(xml_path.read_text())
    pretty_xml = dom.toprettyxml()
    pretty_xml_fixture_path = (
        Path(__file__).parent / 'fixtures/output-unzipped' / zip_path
    )
    assert pretty_xml.strip() == \
        pretty_xml_fixture_path.read_text().strip(), \
        f'Update "{pretty_xml_fixture_path.name}" fixture?'


def test_create_xlsx():
    schema_path = Path(__file__).parent / 'fixtures/schema.yaml'
    schema = safe_load(schema_path.read_text())
    with TemporaryDirectory() as temp_dir_name:
        xlsx_path = Path(temp_dir_name) / 'template.xlsx'
        create_xlsx(schema, xlsx_path)

        assert_xmls_match(xlsx_path, 'xl/worksheets/sheet1.xml')
        assert_xmls_match(xlsx_path, 'xl/sharedStrings.xml')
        assert_xmls_match(xlsx_path, 'xl/comments1.xml')
