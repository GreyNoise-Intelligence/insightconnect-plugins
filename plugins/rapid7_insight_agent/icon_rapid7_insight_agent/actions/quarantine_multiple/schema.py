# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Quarantine or unquarantine multiple hosts"


class Input:
    AGENT_ARRAY = "agent_array"
    INTERVAL = "interval"
    QUARANTINE_STATE = "quarantine_state"
    

class Output:
    ALL_OPERATIONS_SUCCEEDED = "all_operations_succeeded"
    FAILURE = "failure"
    SUCCESS = "success"
    

class QuarantineMultipleInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent_array": {
      "type": "array",
      "title": "Agent Array",
      "description": "Agent hostnames to quarantine or unquarantine",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "interval": {
      "type": "integer",
      "title": "Interval",
      "description": "Length of time in seconds to try to take action on a device. This is also called Advertisement Period",
      "default": 604800,
      "order": 2
    },
    "quarantine_state": {
      "type": "boolean",
      "title": "Quarantine State",
      "description": "Set to true to quarantine a host, set to false to unquarantine",
      "default": true,
      "order": 3
    }
  },
  "required": [
    "agent_array",
    "interval",
    "quarantine_state"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QuarantineMultipleOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "all_operations_succeeded": {
      "type": "boolean",
      "title": "All Operations Succeeded",
      "description": "Informs a user any operations failed the (un)quarantine operations",
      "order": 3
    },
    "failure": {
      "type": "array",
      "title": "Unsuccessful (Un)Quarantine",
      "description": "List of unsuccessfully quarantined hosts",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "success": {
      "type": "array",
      "title": "Successful (Un)Quarantine",
      "description": "List of successfully quarantined hosts",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)