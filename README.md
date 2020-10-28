# tableschema-to-excel-template
Given a [Frictionless Table Schema](https://specs.frictionlessdata.io/table-schema/),
generate an Excel template with input validation. An example of the output is in the [fixtures](tests/fixtures/template.xlsx).

This is a proof of concept.
The biggest challenge I see is how, and whether, to validate regex patterns.
Possibilities:
- Don't even try!
- Add VBA to provide regex support in Excel.
- Target Google Sheets, which provides a regex function out of the box.
- Or target OpenOffice, where [regexes can be turned on in the settings](https://wiki.openoffice.org/wiki/Documentation/OOo3_User_Guides/Calc_Guide/Using_regular_expressions_in_functions).

## Related work

- [csv-gg](https://github.com/etalab/csv-gg): Hits an API to validate rows in a spreadsheet.
- [table-schema-resource-template](https://pypi.org/project/table-schema-resource-template/): Just adds titles to the columns, based on the schema.
- [data-curator](https://github.com/qcif/data-curator): Installable desktop application for data entry, base on schema. 
