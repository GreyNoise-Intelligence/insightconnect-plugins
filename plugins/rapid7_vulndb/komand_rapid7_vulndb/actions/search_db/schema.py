# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search the database to find vulnerabilities and exploits"


class Input:
    DATABASE = "database"
    SEARCH = "search"
    

class Output:
    RESULTS_FOUND = "results_found"
    SEARCH_RESULTS = "search_results"
    

class SearchDbInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "database": {
      "type": "string",
      "title": "Database",
      "description": "Name of the database",
      "enum": [
        "Vulnerability Database",
        "Metasploit Modules"
      ],
      "order": 1
    },
    "search": {
      "type": "string",
      "title": "Search",
      "description": "Search parameter for database",
      "order": 2
    }
  },
  "required": [
    "database",
    "search"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchDbOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results_found": {
      "type": "boolean",
      "title": "Results Found",
      "description": "Will return false if no results are found",
      "order": 2
    },
    "search_results": {
      "type": "array",
      "title": "Results",
      "description": "Vulnerability and exploits found",
      "items": {
        "$ref": "#/definitions/search_result"
      },
      "order": 1
    }
  },
  "required": [
    "results_found"
  ],
  "definitions": {
    "search_result": {
      "type": "object",
      "title": "search_result",
      "properties": {
        "identifier": {
          "type": "string",
          "title": "Content Identifier",
          "description": "Content identifier for module or vulnerability",
          "order": 4
        },
        "link": {
          "type": "string",
          "title": "Link",
          "description": "Link to vulnerability",
          "order": 2
        },
        "published_at": {
          "type": "string",
          "title": "Published At",
          "description": "Published date of vulnerability",
          "order": 3
        },
        "solutions": {
          "type": "string",
          "title": "Solutions",
          "description": "List of possible solutions for the vulnerability",
          "order": 5
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title of vulnerability",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)