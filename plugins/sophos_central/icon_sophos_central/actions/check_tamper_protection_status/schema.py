# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get tamper status by IP address, Hostname, MAC address or Device ID"


class Input:
    AGENT = "agent"


class Output:
    TAMPER_STATUS = "tamper_status"


class CheckTamperProtectionStatusInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Device ID, IPv4 address, IPv6 address, MAC address or hostname",
      "order": 1
    }
  },
  "required": [
    "agent"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckTamperProtectionStatusOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tamper_status": {
      "$ref": "#/definitions/check_tamper_protection_status",
      "title": "Tamper Status",
      "description": "Tamper status for provided agent",
      "order": 1
    }
  },
  "required": [
    "tamper_status"
  ],
  "definitions": {
    "check_tamper_protection_status": {
      "type": "object",
      "title": "check_tamper_protection_status",
      "properties": {
        "enabled": {
          "type": "boolean",
          "title": "Enabled",
          "description": "Return true when tamper protection is enable",
          "order": 1
        }
      },
      "required": [
        "enabled"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
