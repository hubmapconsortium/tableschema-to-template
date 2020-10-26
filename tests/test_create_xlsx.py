from pathlib import Path
from tempfile import TemporaryDirectory
from yaml import safe_load

from create_xlsx import create_xlsx


def test_create_xlsx():
    schema_path = Path(__file__).parent / 'fixtures/schema.yaml'
    schema = safe_load(schema_path.read_text())
    with TemporaryDirectory() as temp_dir_name:
        xlsx_path = Path(temp_dir_name) / 'template.xlsx'
        create_xlsx(schema, xlsx_path)
