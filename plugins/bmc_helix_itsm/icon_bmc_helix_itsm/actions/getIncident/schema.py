# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get detailed information about an BMC Helix ITSM incident"


class Input:
    INCIDENTNUMBER = "incidentNumber"
    

class Output:
    INCIDENT = "incident"
    

class GetIncidentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incidentNumber": {
      "type": "string",
      "title": "Incident Number",
      "description": "Number of the incident",
      "order": 1
    }
  },
  "required": [
    "incidentNumber"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIncidentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident": {
      "$ref": "#/definitions/incident",
      "title": "Incident",
      "description": "Details about the incident",
      "order": 1
    }
  },
  "required": [
    "incident"
  ],
  "definitions": {
    "incident": {
      "type": "object",
      "title": "incident",
      "properties": {
        "assignee": {
          "type": "string",
          "title": "Assignee",
          "description": "Assignee",
          "order": 4
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 10
        },
        "entryId": {
          "type": "string",
          "title": "Entry ID",
          "description": "Entry ID",
          "order": 1
        },
        "impact": {
          "type": "string",
          "title": "Impact",
          "description": "Impact",
          "order": 14
        },
        "incidentNumber": {
          "type": "string",
          "title": "Incident Number",
          "description": "Incident number",
          "order": 12
        },
        "lastModifiedBy": {
          "type": "string",
          "title": "Last Modified By",
          "description": "Last modified by",
          "order": 5
        },
        "lastModifiedDate": {
          "type": "string",
          "title": "Last Modified Date",
          "description": "Last modified date",
          "order": 6
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "Priority",
          "order": 15
        },
        "reportedDate": {
          "type": "string",
          "title": "Reported Date",
          "description": "Reported date",
          "order": 18
        },
        "reportedSource": {
          "type": "string",
          "title": "Reported Source",
          "description": "Reported source",
          "order": 16
        },
        "resolution": {
          "type": "string",
          "title": "Resolution",
          "description": "Resolution",
          "order": 11
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 7
        },
        "statusHistory": {
          "type": "array",
          "title": "Status History",
          "description": "Status history",
          "items": {
            "type": "object"
          },
          "order": 9
        },
        "statusReason": {
          "type": "string",
          "title": "Status Reason",
          "description": "Status reaspm",
          "order": 8
        },
        "submitDate": {
          "type": "string",
          "title": "Submit Date",
          "description": "Submit date",
          "order": 3
        },
        "submitter": {
          "type": "string",
          "title": "Submitter",
          "description": "Submitter",
          "order": 2
        },
        "timeZone": {
          "type": "string",
          "title": "Time Zone",
          "description": "Time zone",
          "order": 17
        },
        "urgency": {
          "type": "string",
          "title": "Urgency",
          "description": "Urgency",
          "order": 13
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)