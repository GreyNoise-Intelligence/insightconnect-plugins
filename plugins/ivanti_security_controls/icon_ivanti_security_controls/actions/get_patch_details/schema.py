# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve information about a patch from Ivanti Security Control"


class Input:
    ID = "id"


class Output:
    PATCH = "patch"


class GetPatchDetailsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "The vulnerability ID",
      "order": 1
    }
  },
  "required": [
    "id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPatchDetailsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "patch": {
      "$ref": "#/definitions/vulnerability",
      "title": "Patch",
      "description": "Detailed information about a patch",
      "order": 1
    }
  },
  "required": [
    "patch"
  ],
  "definitions": {
    "vulnerability": {
      "type": "object",
      "title": "vulnerability",
      "properties": {
        "bulletinId": {
          "type": "string",
          "title": "Bulletin ID",
          "description": "Bulletinid",
          "order": 1
        },
        "cve": {
          "type": "array",
          "title": "CVE",
          "description": "CVE",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "Patch ID",
          "description": "Id",
          "order": 3
        },
        "isSupported": {
          "type": "boolean",
          "title": "Is Supported",
          "description": "Issupported",
          "order": 4
        },
        "kb": {
          "type": "string",
          "title": "Kb",
          "description": "Kb",
          "order": 5
        },
        "links": {
          "$ref": "#/definitions/links_self",
          "title": "Links",
          "description": "Links",
          "order": 6
        },
        "patchIds": {
          "type": "array",
          "title": "Patchids",
          "description": "Patch IDs",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "patchType": {
          "type": "string",
          "title": "Patchtype",
          "description": "Patch Type",
          "order": 8
        },
        "releaseDate": {
          "type": "string",
          "title": "Releasedate",
          "description": "Release Date",
          "order": 9
        },
        "replacedBy": {
          "type": "array",
          "title": "Replaced By",
          "description": "Replacedby",
          "items": {
            "type": "string"
          },
          "order": 10
        }
      }
    },
    "links_self": {
      "type": "object",
      "title": "links_self",
      "properties": {
        "self": {
          "$ref": "#/definitions/next",
          "title": "Self",
          "description": "Self",
          "order": 1
        }
      }
    },
    "next": {
      "type": "object",
      "title": "next",
      "properties": {
        "href": {
          "type": "string",
          "title": "HREF",
          "description": "Href",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
