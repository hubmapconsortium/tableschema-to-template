# tableschema-to-template

Given a [Frictionless Table Schema](https://specs.frictionlessdata.io/table-schema/)
(like [this](https://raw.githubusercontent.com/hubmapconsortium/tableschema-to-template/main/tests/fixtures/schema.yaml)),
generate an Excel template with input validation
(like [this](https://raw.githubusercontent.com/hubmapconsortium/tableschema-to-template/main/tests/fixtures/template.xlsx)).

## Usage

Download a [sample `schema.yaml`](https://raw.githubusercontent.com/hubmapconsortium/tableschema-to-template/main/tests/fixtures/schema.yaml), and then:

```sh
pip install tableschema-to-template
ts2xl.py schema.yaml template.xlsx
# Open with Excel:
open template.xlsx
```

Or to use inside Python:
```python
from tableschema_to_template.create_xlsx import create_xlsx
schema = {'fields': [{
  'name': 'a_number',
  'description': 'A number!',
  'type': 'number'
}]}
create_xlsx(schema, '/tmp/template.xlsx')
```

[Instructions for project developers here.](https://github.com/hubmapconsortium/tableschema-to-template/blob/main/README-dev.md#readme)

## Features

- Enum constraints transformed into pull-downs.
- Field descriptions transformed into comments in header.
- Float, integer, and boolean type validation.

## Related work

From the Frictionless community:
- [`table-schema-resource-template`](https://pypi.org/project/table-schema-resource-template/): Generates templates, but doesn't go beyond row headers. 
- [`data-curator`](https://github.com/qcif/data-curator): Desktop application for data entry based on Table Schema.
- [`csv-gg`](https://github.com/etalab/csv-gg): Web app which serves data entry form, and uses [Validata API](https://git.opendatafrance.net/validata/) for validation. 

For the biomedical ontologies community:
- [`CEDAR`](https://more.metadatacenter.org/): Data entry tool based on ontologies.
- [`Webulous`](https://www.ebi.ac.uk/spot/webulous/): Google sheets plugin that adds pulldowns based on ontology terms.
