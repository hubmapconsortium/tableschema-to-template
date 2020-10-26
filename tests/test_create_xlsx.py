from pathlib import Path
from tempfile import TemporaryDirectory
import zipfile
import xml.dom.minidom

from yaml import safe_load

from create_xlsx import create_xlsx


def test_create_xlsx():
    schema_path = Path(__file__).parent / 'fixtures/schema.yaml'
    schema = safe_load(schema_path.read_text())
    with TemporaryDirectory() as temp_dir_name:
        xlsx_path = Path(temp_dir_name) / 'template.xlsx'
        create_xlsx(schema, xlsx_path)

        sheet_path = zipfile.Path(xlsx_path, 'xl/worksheets/sheet1.xml')
        dom = xml.dom.minidom.parseString(sheet_path.read_text())
        pretty_xml = dom.toprettyxml()
        pretty_xml_fixture_path = Path(__file__).parent / 'fixtures/sheet1.xml'
        assert pretty_xml.strip() == \
            pretty_xml_fixture_path.read_text().strip()
        # zipfile.Path(xlsx_path, 'xl/worksheets/sheet1.xml')
        # zipfile.Path(xlsx_path, 'xl/worksheets/sheet1.xml')
