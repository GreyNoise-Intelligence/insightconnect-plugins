# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Return the size (number of elements) for every type"


class Input:
    pass

class Output:
    SIZES = "sizes"
    

class SizeByTypeInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SizeByTypeOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "sizes": {
      "type": "array",
      "title": "Sizes",
      "description": "List of types with corresponding sizes",
      "items": {
        "$ref": "#/definitions/size"
      },
      "order": 1
    }
  },
  "required": [
    "sizes"
  ],
  "definitions": {
    "size": {
      "type": "object",
      "title": "size",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of corresponding type or source",
          "order": 1
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "Size",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)