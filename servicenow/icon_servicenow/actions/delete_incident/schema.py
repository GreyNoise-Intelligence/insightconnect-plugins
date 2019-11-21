# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Remove the given ServiceNow Incident from the instance"


class Input:
    SYSTEM_ID = "system_id"
    

class Output:
    SUCCESS = "success"
    

class DeleteIncidentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "system_id": {
      "type": "string",
      "title": "System ID",
      "description": "System ID of the Incident record to delete",
      "order": 1
    }
  },
  "required": [
    "system_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteIncidentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "True if the deletion was successful, false otherwise",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
