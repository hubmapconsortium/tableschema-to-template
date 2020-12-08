from yaml import safe_load
from jsonschema import validate
from jsonschema import ValidationError

from tableschema_to_template import ShowUsageException


def validate_input(table_schema):
    '''
    >>> validate_input({})
    Traceback (most recent call last):
    ...
    tableschema_to_template.ShowUsageException: Not a valid Table Schema: 'fields' ... required property

    (Phrasing of error message changed between versions.)
    '''
    table_schema_schema = safe_load(_table_schema_schema)
    try:
        validate(table_schema, table_schema_schema)
    except ValidationError as e:
        raise ShowUsageException(f'Not a valid Table Schema: {e.message}')


# This is ugly, but it's less configuration than including JSON in the build.
# From: https://specs.frictionlessdata.io/schemas/table-schema.json
_table_schema_schema = r'''
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "Table Schema",
  "description": "A Table Schema for this resource, compliant with the [Table Schema](/tableschema/) specification.",
  "type": "object",
  "required": [
    "fields"
  ],
  "properties": {
    "fields": {
      "type": "array",
      "minItems": 1,
      "items": {
        "title": "Table Schema Field",
        "type": "object",
        "anyOf": [
          {
            "type": "object",
            "title": "String Field",
            "description": "The field contains strings, that is, sequences of characters.",
            "required": [
              "name"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `string`.",
                "enum": [
                  "string"
                ]
              },
              "format": {
                "description": "The format keyword options for `string` are `default`, `email`, `uri`, `binary`, and `uuid`.",
                "context": "The following `format` options are supported:\n  * **default**: any valid string.\n  * **email**: A valid email address.\n  * **uri**: A valid URI.\n  * **binary**: A base64 encoded string representing binary data.\n  * **uuid**: A string that is a uuid.",
                "enum": [
                  "default",
                  "email",
                  "uri",
                  "binary",
                  "uuid"
                ],
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `string` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "pattern": {
                    "type": "string",
                    "description": "A regular expression pattern to test each value of the property against, where a truthy response indicates validity.",
                    "context": "Regular expressions `SHOULD` conform to the [XML Schema regular expression syntax](http://www.w3.org/TR/xmlschema-2/#regexs)."
                  },
                  "enum": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": true,
                    "items": {
                      "type": "string"
                    }
                  },
                  "minLength": {
                    "type": "integer",
                    "description": "An integer that specifies the minimum length of a value."
                  },
                  "maxLength": {
                    "type": "integer",
                    "description": "An integer that specifies the maximum length of a value."
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"name\",\n  \"type\": \"string\"\n}\n",
              "{\n  \"name\": \"name\",\n  \"type\": \"string\",\n  \"format\": \"email\"\n}\n",
              "{\n  \"name\": \"name\",\n  \"type\": \"string\",\n  \"constraints\": {\n    \"minLength\": 3,\n    \"maxLength\": 35\n  }\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Number Field",
            "description": "The field contains numbers of any kind including decimals.",
            "context": "The lexical formatting follows that of decimal in [XMLSchema](https://www.w3.org/TR/xmlschema-2/#decimal): a non-empty finite-length sequence of decimal digits separated by a period as a decimal indicator. An optional leading sign is allowed. If the sign is omitted, '+' is assumed. Leading and trailing zeroes are optional. If the fractional part is zero, the period and following zero(es) can be omitted. For example: '-1.23', '12678967.543233', '+100000.00', '210'.\n\nThe following special string values are permitted (case does not need to be respected):\n  - NaN: not a number\n  - INF: positive infinity\n  - -INF: negative infinity\n\nA number `MAY` also have a trailing:\n  - exponent: this `MUST` consist of an E followed by an optional + or - sign followed by one or more decimal digits (0-9)\n  - percentage: the percentage sign: `%`. In conversion percentages should be divided by 100.\n\nIf both exponent and percentages are present the percentage `MUST` follow the exponent e.g. '53E10%' (equals 5.3).",
            "required": [
              "name"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `number`.",
                "enum": [
                  "number"
                ]
              },
              "format": {
                "description": "There are no format keyword options for `number`: only `default` is allowed.",
                "enum": [
                  "default"
                ],
                "default": "default"
              },
              "bareNumber": {
                "type": "boolean",
                "title": "bareNumber",
                "description": "a boolean field with a default of `true`. If `true` the physical contents of this field must follow the formatting constraints already set out. If `false` the contents of this field may contain leading and/or trailing non-numeric characters (which implementors MUST therefore strip). The purpose of `bareNumber` is to allow publishers to publish numeric data that contains trailing characters such as percentages e.g. `95%` or leading characters such as currencies e.g. `€95` or `EUR 95`. Note that it is entirely up to implementors what, if anything, they do with stripped text.",
                "default": true
              },
              "decimalChar": {
                "type": "string",
                "description": "A string whose value is used to represent a decimal point within the number. The default value is `.`."
              },
              "groupChar": {
                "type": "string",
                "description": "A string whose value is used to group digits within the number. The default value is `null`. A common value is `,` e.g. '100,000'."
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `number` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "oneOf": [
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "string"
                        }
                      },
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "number"
                        }
                      }
                    ]
                  },
                  "minimum": {
                    "oneOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "number"
                      }
                    ]
                  },
                  "maximum": {
                    "oneOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "number"
                      }
                    ]
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"field-name\",\n  \"type\": \"number\"\n}\n",
              "{\n  \"name\": \"field-name\",\n  \"type\": \"number\",\n  \"constraints\": {\n    \"enum\": [ \"1.00\", \"1.50\", \"2.00\" ]\n  }\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Integer Field",
            "description": "The field contains integers - that is whole numbers.",
            "context": "Integer values are indicated in the standard way for any valid integer.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `integer`.",
                "enum": [
                  "integer"
                ]
              },
              "format": {
                "description": "There are no format keyword options for `integer`: only `default` is allowed.",
                "enum": [
                  "default"
                ],
                "default": "default"
              },
              "bareNumber": {
                "type": "boolean",
                "title": "bareNumber",
                "description": "a boolean field with a default of `true`. If `true` the physical contents of this field must follow the formatting constraints already set out. If `false` the contents of this field may contain leading and/or trailing non-numeric characters (which implementors MUST therefore strip). The purpose of `bareNumber` is to allow publishers to publish numeric data that contains trailing characters such as percentages e.g. `95%` or leading characters such as currencies e.g. `€95` or `EUR 95`. Note that it is entirely up to implementors what, if anything, they do with stripped text.",
                "default": true
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `integer` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "oneOf": [
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "string"
                        }
                      },
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "integer"
                        }
                      }
                    ]
                  },
                  "minimum": {
                    "oneOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "integer"
                      }
                    ]
                  },
                  "maximum": {
                    "oneOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "integer"
                      }
                    ]
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"age\",\n  \"type\": \"integer\",\n  \"constraints\": {\n    \"unique\": true,\n    \"minimum\": 100,\n    \"maximum\": 9999\n  }\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Date Field",
            "description": "The field contains temporal date values.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `date`.",
                "enum": [
                  "date"
                ]
              },
              "format": {
                "description": "The format keyword options for `date` are `default`, `any`, and `{PATTERN}`.",
                "context": "The following `format` options are supported:\n  * **default**: An ISO8601 format string of YYYY-MM-DD.\n  * **any**: Any parsable representation of a date. The implementing library can attempt to parse the datetime via a range of strategies.\n  * **{PATTERN}**: The value can be parsed according to `{PATTERN}`, which `MUST` follow the date formatting syntax of C / Python [strftime](http://strftime.org/).",
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `date` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": true,
                    "items": {
                      "type": "string"
                    }
                  },
                  "minimum": {
                    "type": "string"
                  },
                  "maximum": {
                    "type": "string"
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"date_of_birth\",\n  \"type\": \"date\"\n}\n",
              "{\n  \"name\": \"date_of_birth\",\n  \"type\": \"date\",\n  \"constraints\": {\n    \"minimum\": \"01-01-1900\"\n  }\n}\n",
              "{\n  \"name\": \"date_of_birth\",\n  \"type\": \"date\",\n  \"format\": \"MM-DD-YYYY\"\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Time Field",
            "description": "The field contains temporal time values.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `time`.",
                "enum": [
                  "time"
                ]
              },
              "format": {
                "description": "The format keyword options for `time` are `default`, `any`, and `{PATTERN}`.",
                "context": "The following `format` options are supported:\n  * **default**: An ISO8601 format string for time.\n  * **any**: Any parsable representation of a date. The implementing library can attempt to parse the datetime via a range of strategies.\n  * **{PATTERN}**: The value can be parsed according to `{PATTERN}`, which `MUST` follow the date formatting syntax of C / Python [strftime](http://strftime.org/).",
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `time` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": true,
                    "items": {
                      "type": "string"
                    }
                  },
                  "minimum": {
                    "type": "string"
                  },
                  "maximum": {
                    "type": "string"
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"appointment_start\",\n  \"type\": \"time\"\n}\n",
              "{\n  \"name\": \"appointment_start\",\n  \"type\": \"time\",\n  \"format\": \"any\"\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Date Time Field",
            "description": "The field contains temporal datetime values.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `datetime`.",
                "enum": [
                  "datetime"
                ]
              },
              "format": {
                "description": "The format keyword options for `datetime` are `default`, `any`, and `{PATTERN}`.",
                "context": "The following `format` options are supported:\n  * **default**: An ISO8601 format string for datetime.\n  * **any**: Any parsable representation of a date. The implementing library can attempt to parse the datetime via a range of strategies.\n  * **{PATTERN}**: The value can be parsed according to `{PATTERN}`, which `MUST` follow the date formatting syntax of C / Python [strftime](http://strftime.org/).",
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `datetime` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": true,
                    "items": {
                      "type": "string"
                    }
                  },
                  "minimum": {
                    "type": "string"
                  },
                  "maximum": {
                    "type": "string"
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"timestamp\",\n  \"type\": \"datetime\"\n}\n",
              "{\n  \"name\": \"timestamp\",\n  \"type\": \"datetime\",\n  \"format\": \"default\"\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Year Field",
            "description": "A calendar year, being an integer with 4 digits. Equivalent to [gYear in XML Schema](https://www.w3.org/TR/xmlschema-2/#gYear)",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `year`.",
                "enum": [
                  "year"
                ]
              },
              "format": {
                "description": "There are no format keyword options for `year`: only `default` is allowed.",
                "enum": [
                  "default"
                ],
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `year` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "oneOf": [
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "string"
                        }
                      },
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "integer"
                        }
                      }
                    ]
                  },
                  "minimum": {
                    "oneOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "integer"
                      }
                    ]
                  },
                  "maximum": {
                    "oneOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "integer"
                      }
                    ]
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"year\",\n  \"type\": \"year\"\n}\n",
              "{\n  \"name\": \"year\",\n  \"type\": \"year\",\n  \"constraints\": {\n    \"minimum\": 1970,\n    \"maximum\": 2003\n  }\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Year Month Field",
            "description": "A calendar year month, being an integer with 1 or 2 digits. Equivalent to [gYearMonth in XML Schema](https://www.w3.org/TR/xmlschema-2/#gYearMonth)",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `yearmonth`.",
                "enum": [
                  "yearmonth"
                ]
              },
              "format": {
                "description": "There are no format keyword options for `yearmonth`: only `default` is allowed.",
                "enum": [
                  "default"
                ],
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `yearmonth` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": true,
                    "items": {
                      "type": "string"
                    }
                  },
                  "minimum": {
                    "type": "string"
                  },
                  "maximum": {
                    "type": "string"
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"month\",\n  \"type\": \"yearmonth\"\n}\n",
              "{\n  \"name\": \"month\",\n  \"type\": \"yearmonth\",\n  \"constraints\": {\n    \"minimum\": 1,\n    \"maximum\": 6\n  }\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Boolean Field",
            "description": "The field contains boolean (true/false) data.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `boolean`.",
                "enum": [
                  "boolean"
                ]
              },
              "trueValues": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "string"
                },
                "default": [
                  "true",
                  "True",
                  "TRUE",
                  "1"
                ]
              },
              "falseValues": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "string"
                },
                "default": [
                  "false",
                  "False",
                  "FALSE",
                  "0"
                ]
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `boolean` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "enum": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": true,
                    "items": {
                      "type": "boolean"
                    }
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"registered\",\n  \"type\": \"boolean\"\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Object Field",
            "description": "The field contains data which can be parsed as a valid JSON object.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `object`.",
                "enum": [
                  "object"
                ]
              },
              "format": {
                "description": "There are no format keyword options for `object`: only `default` is allowed.",
                "enum": [
                  "default"
                ],
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints apply for `object` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "oneOf": [
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "string"
                        }
                      },
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "object"
                        }
                      }
                    ]
                  },
                  "minLength": {
                    "type": "integer",
                    "description": "An integer that specifies the minimum length of a value."
                  },
                  "maxLength": {
                    "type": "integer",
                    "description": "An integer that specifies the maximum length of a value."
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"extra\"\n  \"type\": \"object\"\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "GeoPoint Field",
            "description": "The field contains data describing a geographic point.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `geopoint`.",
                "enum": [
                  "geopoint"
                ]
              },
              "format": {
                "description": "The format keyword options for `geopoint` are `default`,`array`, and `object`.",
                "context": "The following `format` options are supported:\n  * **default**: A string of the pattern 'lon, lat', where `lon` is the longitude and `lat` is the latitude.\n  * **array**: An array of exactly two items, where each item is either a number, or a string parsable as a number, and the first item is `lon` and the second item is `lat`.\n  * **object**: A JSON object with exactly two keys, `lat` and `lon`",
                "notes": [
                  "Implementations `MUST` strip all white space in the default format of `lon, lat`."
                ],
                "enum": [
                  "default",
                  "array",
                  "object"
                ],
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `geopoint` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "oneOf": [
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "string"
                        }
                      },
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "array"
                        }
                      },
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "object"
                        }
                      }
                    ]
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"post_office\",\n  \"type\": \"geopoint\"\n}\n",
              "{\n  \"name\": \"post_office\",\n  \"type\": \"geopoint\",\n  \"format\": \"array\"\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "GeoJSON Field",
            "description": "The field contains a JSON object according to GeoJSON or TopoJSON",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `geojson`.",
                "enum": [
                  "geojson"
                ]
              },
              "format": {
                "description": "The format keyword options for `geojson` are `default` and `topojson`.",
                "context": "The following `format` options are supported:\n  * **default**: A geojson object as per the [GeoJSON spec](http://geojson.org/).\n  * **topojson**: A topojson object as per the [TopoJSON spec](https://github.com/topojson/topojson-specification/blob/master/README.md)",
                "enum": [
                  "default",
                  "topojson"
                ],
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `geojson` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "oneOf": [
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "string"
                        }
                      },
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "object"
                        }
                      }
                    ]
                  },
                  "minLength": {
                    "type": "integer",
                    "description": "An integer that specifies the minimum length of a value."
                  },
                  "maxLength": {
                    "type": "integer",
                    "description": "An integer that specifies the maximum length of a value."
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"city_limits\",\n  \"type\": \"geojson\"\n}\n",
              "{\n  \"name\": \"city_limits\",\n  \"type\": \"geojson\",\n  \"format\": \"topojson\"\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Array Field",
            "description": "The field contains data which can be parsed as a valid JSON array.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `array`.",
                "enum": [
                  "array"
                ]
              },
              "format": {
                "description": "There are no format keyword options for `array`: only `default` is allowed.",
                "enum": [
                  "default"
                ],
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints apply for `array` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "oneOf": [
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "string"
                        }
                      },
                      {
                        "type": "array",
                        "minItems": 1,
                        "uniqueItems": true,
                        "items": {
                          "type": "array"
                        }
                      }
                    ]
                  },
                  "minLength": {
                    "type": "integer",
                    "description": "An integer that specifies the minimum length of a value."
                  },
                  "maxLength": {
                    "type": "integer",
                    "description": "An integer that specifies the maximum length of a value."
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"options\"\n  \"type\": \"array\"\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Duration Field",
            "description": "The field contains a duration of time.",
            "context": "The lexical representation for duration is the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations) extended format `PnYnMnDTnHnMnS`, where `nY` represents the number of years, `nM` the number of months, `nD` the number of days, 'T' is the date/time separator, `nH` the number of hours, `nM` the number of minutes and `nS` the number of seconds. The number of seconds can include decimal digits to arbitrary precision. Date and time elements including their designator may be omitted if their value is zero, and lower order elements may also be omitted for reduced precision. Here we follow the definition of [XML Schema duration datatype](http://www.w3.org/TR/xmlschema-2/#duration) directly and that definition is implicitly inlined here.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `duration`.",
                "enum": [
                  "duration"
                ]
              },
              "format": {
                "description": "There are no format keyword options for `duration`: only `default` is allowed.",
                "enum": [
                  "default"
                ],
                "default": "default"
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints are supported for `duration` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": true,
                    "items": {
                      "type": "string"
                    }
                  },
                  "minimum": {
                    "type": "string"
                  },
                  "maximum": {
                    "type": "string"
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"period\"\n  \"type\": \"duration\"\n}\n"
            ]
          },
          {
            "type": "object",
            "title": "Any Field",
            "description": "Any value is accepted, including values that are not captured by the type/format/constraint requirements of the specification.",
            "required": [
              "name",
              "type"
            ],
            "properties": {
              "name": {
                "title": "Name",
                "description": "A name for this field.",
                "type": "string"
              },
              "title": {
                "title": "Title",
                "description": "A human-readable title.",
                "type": "string",
                "examples": [
                  "{\n  \"title\": \"My Package Title\"\n}\n"
                ]
              },
              "description": {
                "title": "Description",
                "description": "A text description. Markdown is encouraged.",
                "type": "string",
                "examples": [
                  "{\n  \"description\": \"# My Package description\\nAll about my package.\"\n}\n"
                ]
              },
              "type": {
                "description": "The type keyword, which `MUST` be a value of `any`.",
                "enum": [
                  "any"
                ]
              },
              "constraints": {
                "title": "Constraints",
                "description": "The following constraints apply to `any` fields.",
                "type": "object",
                "properties": {
                  "required": {
                    "type": "boolean",
                    "description": "Indicates whether a property must have a value for each instance.",
                    "context": "An empty string is considered to be a missing value."
                  },
                  "unique": {
                    "type": "boolean",
                    "description": "When `true`, each value for the property `MUST` be unique."
                  },
                  "enum": {
                    "type": "array",
                    "minItems": 1,
                    "uniqueItems": true
                  }
                }
              },
              "rdfType": {
                "type": "string",
                "description": "The RDF type for this field."
              }
            },
            "examples": [
              "{\n  \"name\": \"notes\",\n  \"type\": \"any\"\n"
            ]
          }
        ]
      },
      "description": "An `array` of Table Schema Field objects.",
      "examples": [
        "{\n  \"fields\": [\n    {\n      \"name\": \"my-field-name\"\n    }\n  ]\n}\n",
        "{\n  \"fields\": [\n    {\n      \"name\": \"my-field-name\",\n      \"type\": \"number\"\n    },\n    {\n      \"name\": \"my-field-name-2\",\n      \"type\": \"string\",\n      \"format\": \"email\"\n    }\n  ]\n}\n"
      ]
    },
    "primaryKey": {
      "oneOf": [
        {
          "type": "array",
          "minItems": 1,
          "uniqueItems": true,
          "items": {
            "type": "string"
          }
        },
        {
          "type": "string"
        }
      ],
      "description": "A primary key is a field name or an array of field names, whose values `MUST` uniquely identify each row in the table.",
      "context": "Field name in the `primaryKey` `MUST` be unique, and `MUST` match a field name in the associated table. It is acceptable to have an array with a single value, indicating that the value of a single field is the primary key.",
      "examples": [
        "{\n  \"primaryKey\": [\n    \"name\"\n  ]\n}\n",
        "{\n  \"primaryKey\": [\n    \"first_name\",\n    \"last_name\"\n  ]\n}\n"
      ]
    },
    "foreignKeys": {
      "type": "array",
      "minItems": 1,
      "items": {
        "title": "Table Schema Foreign Key",
        "description": "Table Schema Foreign Key",
        "type": "object",
        "required": [
          "fields",
          "reference"
        ],
        "oneOf": [
          {
            "properties": {
              "fields": {
                "type": "array",
                "items": {
                  "type": "string",
                  "minItems": 1,
                  "uniqueItems": true,
                  "description": "Fields that make up the primary key."
                }
              },
              "reference": {
                "type": "object",
                "required": [
                  "resource",
                  "fields"
                ],
                "properties": {
                  "resource": {
                    "type": "string",
                    "default": ""
                  },
                  "fields": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "minItems": 1,
                    "uniqueItems": true
                  }
                }
              }
            }
          },
          {
            "properties": {
              "fields": {
                "type": "string",
                "description": "Fields that make up the primary key."
              },
              "reference": {
                "type": "object",
                "required": [
                  "resource",
                  "fields"
                ],
                "properties": {
                  "resource": {
                    "type": "string",
                    "default": ""
                  },
                  "fields": {
                    "type": "string"
                  }
                }
              }
            }
          }
        ]
      },
      "examples": [
        "{\n  \"foreignKeys\": [\n    {\n      \"fields\": \"state\",\n      \"reference\": {\n        \"resource\": \"the-resource\",\n        \"fields\": \"state_id\"\n      }\n    }\n  ]\n}\n",
        "{\n  \"foreignKeys\": [\n    {\n      \"fields\": \"state\",\n      \"reference\": {\n        \"resource\": \"\",\n        \"fields\": \"id\"\n      }\n    }\n  ]\n}\n"
      ]
    },
    "missingValues": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "default": [
        ""
      ],
      "description": "Values that when encountered in the source, should be considered as `null`, 'not present', or 'blank' values.",
      "context": "Many datasets arrive with missing data values, either because a value was not collected or it never existed.\nMissing values may be indicated simply by the value being empty in other cases a special value may have been used e.g. `-`, `NaN`, `0`, `-9999` etc.\nThe `missingValues` property provides a way to indicate that these values should be interpreted as equivalent to null.\n\n`missingValues` are strings rather than being the data type of the particular field. This allows for comparison prior to casting and for fields to have missing value which are not of their type, for example a `number` field to have missing values indicated by `-`.\n\nThe default value of `missingValue` for a non-string type field is the empty string `''`. For string type fields there is no default for `missingValue` (for string fields the empty string `''` is a valid value and need not indicate null).",
      "examples": [
        "{\n  \"missingValues\": [\n    \"-\",\n    \"NaN\",\n    \"\"\n  ]\n}\n",
        "{\n  \"missingValues\": []\n}\n"
      ]
    }
  },
  "examples": [
    "{\n  \"schema\": {\n    \"fields\": [\n      {\n        \"name\": \"first_name\",\n        \"type\": \"string\"\n        \"constraints\": {\n          \"required\": true\n        }\n      },\n      {\n        \"name\": \"age\",\n        \"type\": \"integer\"\n      },\n    ],\n    \"primaryKey\": [\n      \"name\"\n    ]\n  }\n}\n"
  ]
}
'''
