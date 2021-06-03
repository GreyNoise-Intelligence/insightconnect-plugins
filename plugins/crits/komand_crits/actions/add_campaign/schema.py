# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Creates a new campaign"


class Input:
    NAME = "name"
    PARAMS = "params"
    

class Output:
    RESPONSE = "response"
    

class AddCampaignInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of the campaign",
      "order": 1
    },
    "params": {
      "type": "object",
      "title": "Parameters",
      "description": "Object containing related data or metadata",
      "order": 2
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddCampaignOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/post_response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "post_response": {
      "type": "object",
      "title": "post_response",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "order": 1
        },
        "message": {
          "type": "string",
          "title": "Message",
          "order": 2
        },
        "return_code": {
          "type": "integer",
          "title": "Return Code",
          "description": "The return_code is usually 0 for success, 1 for failure",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The TLO type of the TLO that created or updated",
          "order": 3
        },
        "url": {
          "type": "string",
          "title": "URL",
          "order": 5
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)