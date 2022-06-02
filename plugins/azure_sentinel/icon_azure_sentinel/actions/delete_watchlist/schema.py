# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Delete requested watchlist"


class Input:
    RESOURCEGROUPNAME = "resourceGroupName"
    SUBSCRIPTIONID = "subscriptionId"
    WATCHLISTALIAS = "watchlistAlias"
    WORKSPACENAME = "workspaceName"
    

class Output:
    STATUS = "status"
    

class DeleteWatchlistInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "resourceGroupName": {
      "type": "string",
      "title": "Resource Group Name",
      "description": "The name of the resource group within the user's subscription. The name is case insensitive",
      "order": 1
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "Azure subscription ID",
      "order": 2
    },
    "watchlistAlias": {
      "type": "string",
      "title": "Watchlist Alias",
      "description": "The watchlist alias",
      "order": 4
    },
    "workspaceName": {
      "type": "string",
      "title": "Workspace Name",
      "description": "The name of the workspace",
      "order": 3
    }
  },
  "required": [
    "resourceGroupName",
    "subscriptionId",
    "watchlistAlias",
    "workspaceName"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteWatchlistOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "integer",
      "title": "Deletion Status",
      "description": "Deletion status, 200 - ok, 204 - no content",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)