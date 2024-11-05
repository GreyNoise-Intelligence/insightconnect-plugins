# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Deploy IPS rules"


class Input:
    COMPUTER_OR_POLICY = "computer_or_policy"
    ID = "id"
    RULES = "rules"


class Output:
    RULES_ASSIGNED = "rules_assigned"
    RULES_NOT_ASSIGNED = "rules_not_assigned"


class DeployRulesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "computer_or_policy": {
      "type": "string",
      "title": "Target",
      "description": "Target for rule assignment",
      "enum": [
        "computer",
        "policy"
      ],
      "order": 1
    },
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID of the target computer or policy",
      "order": 2
    },
    "rules": {
      "type": "array",
      "title": "IPS Rules",
      "description": "IPS rules to assign",
      "items": {
        "type": "integer"
      },
      "order": 3
    }
  },
  "required": [
    "computer_or_policy",
    "id",
    "rules"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeployRulesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "rules_assigned": {
      "type": "array",
      "title": "Rules Assigned",
      "description": "All IPS rules currently assigned",
      "items": {
        "type": "integer"
      },
      "order": 1
    },
    "rules_not_assigned": {
      "type": "array",
      "title": "Not Assigned Rules",
      "description": "Unassigned IPS rules",
      "items": {
        "type": "integer"
      },
      "order": 2
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
