# tableschema-to-excel-template
Given a [Frictionless Table Schema](https://specs.frictionlessdata.io/table-schema/),
generate an Excel template with input validation. An example of the output is in the [fixtures](tests/fixtures/template.xlsx).

This is a proof of concept.

## Challenges
The biggest challenge I see is how, and whether, to validate regex patterns.
Possibilities:
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
- [`CEDAR`](https://more.metadatacenter.org/)

