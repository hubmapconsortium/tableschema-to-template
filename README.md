# tableschema-to-template

Given a [Frictionless Table Schema](https://specs.frictionlessdata.io/table-schema/)
(like [this](https://raw.githubusercontent.com/hubmapconsortium/tableschema-to-template/main/tests/fixtures/schema.yaml)),
generate an Excel template with input validation
(like [this](https://raw.githubusercontent.com/hubmapconsortium/tableschema-to-template/main/tests/fixtures/template.xlsx)).

**This is a proof of concept.**

## Usage

From a checkout of the repo, run a demo:
```
pip install -r requirements.txt
tableschema_to_template/ts2xl.py \
  --input_schema tests/fixtures/schema.yaml \
  --output_dir /tmp
open /tmp/template.xlsx
```

## Development

Run the tests:
```
pip install -r requirements-dev.txt
./test.sh
```

To build and publish,
- If you haven't already, generate a token on Pypi and create a `.pypirc` in your checkout.
- Increment the version number in setup.py.
- Finally: `./publish.sh`

## Next steps

- Package and push to pypi.
- How, and whether, to validate regex patterns. Possibilities:
  - Don't even try!
  - Add VBA to provide regex support in Excel.
  - Target Google Sheets, which provides a regex function out of the box.
  - Or target OpenOffice, where [regexes can be turned on in the settings](https://wiki.openoffice.org/wiki/Documentation/OOo3_User_Guides/Calc_Guide/Using_regular_expressions_in_functions).

## Related work

From the Frictionless community:
- [`table-schema-resource-template`](https://pypi.org/project/table-schema-resource-template/): Generates templates, but doesn't go beyond row headers. 
- [`data-curator`](https://github.com/qcif/data-curator): Desktop application for data entry based on Table Schema.
- [`csv-gg`](https://github.com/etalab/csv-gg): Web app which serves data entry form, and uses [Validata API](https://git.opendatafrance.net/validata/) for validation. 

For the biomedical ontologies community:
- [`CEDAR`](https://more.metadatacenter.org/): Data entry tool based on ontologies.
- [`Webulous`](https://www.ebi.ac.uk/spot/webulous/): Google sheets plugin that adds pulldowns based on ontology terms.
