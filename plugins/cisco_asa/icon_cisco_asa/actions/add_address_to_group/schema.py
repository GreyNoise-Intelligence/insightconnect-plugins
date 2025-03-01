# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add an Object to a Network Group by the Object IP address"


class Input:
    ADDRESS = "address"
    GROUP = "group"


class Output:
    SUCCESS = "success"


class AddAddressToGroupInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "Name of the address, which can be an IPv4 or IPv6 address",
      "order": 1
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Name of the group to add the address to",
      "order": 2
    }
  },
  "required": [
    "address",
    "group"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddAddressToGroupOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success if address add to group",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
