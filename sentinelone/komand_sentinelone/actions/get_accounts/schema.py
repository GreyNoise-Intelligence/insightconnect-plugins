# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get a list of accounts"


class Input:
    ACCOUNT_IDS = "account_ids"
    ACCOUNT_TYPE = "account_type"
    ACTIVE_LICENSES = "active_licenses"
    COUNT_ONLY = "count_only"
    CREATED_AT = "created_at"
    CURSOR = "cursor"
    EXPIRATION = "expiration"
    FEATURES = "features"
    IDS = "ids"
    IS_DEFAULT = "is_default"
    LIMIT = "limit"
    NAME = "name"
    QUERY = "query"
    SKIP = "skip"
    SKIP_COUNT = "skip_count"
    SORT_BY = "sort_by"
    SORT_ORDER = "sort_order"
    STATES = "states"
    TOTAL_LICENSES = "total_licenses"
    UPDATED_AT = "updated_at"
    

class Output:
    DATA = "data"
    PAGINATION = "pagination"
    

class GetAccountsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "account_ids": {
      "type": "array",
      "title": "Account IDs",
      "description": "List of account IDs to search for. Example 225494730938493804,225494730938493915",
      "items": {
        "type": "string"
      },
      "order": 13
    },
    "account_type": {
      "type": "string",
      "title": "Account Type",
      "description": "Account type. Example Trial",
      "enum": [
        "Trial",
        "Paid"
      ],
      "order": 5
    },
    "active_licenses": {
      "type": "integer",
      "title": "Active Licenses",
      "description": "How much licenses are active",
      "order": 2
    },
    "count_only": {
      "type": "boolean",
      "title": "Count Only",
      "description": "If true, only total number of items will be returned, without any of the actual objects",
      "order": 17
    },
    "created_at": {
      "type": "string",
      "title": "Created At",
      "description": "Timestamp of account creation. Example 2018-02-27T04:49:26.257525Z",
      "order": 14
    },
    "cursor": {
      "type": "string",
      "title": "Cursor",
      "description": "Cursor position returned by the last request. Should be used for iterating over more than 1000 items. Example YWdlbnRfaWQ6NTgwMjkzODE=",
      "order": 4
    },
    "expiration": {
      "type": "string",
      "title": "Expiration",
      "description": "When account should expire, example: 2018-02-27T04:49:26.257525Z",
      "order": 6
    },
    "features": {
      "type": "array",
      "title": "Features",
      "description": "If sent return only accounts that support this features. Example firewall-control",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "ids": {
      "type": "array",
      "title": "IDs",
      "description": "A list of account IDs. Example 225494730938493804,225494730938493915",
      "items": {
        "type": "string"
      },
      "order": 8
    },
    "is_default": {
      "type": "boolean",
      "title": "Is Default",
      "description": "Filter by default",
      "order": 19
    },
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Limit number of returned items (1-100). Example 10",
      "order": 16
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name. Example My Account",
      "order": 12
    },
    "query": {
      "type": "string",
      "title": "Query",
      "description": "Full text search for fields name. Note on single-account consoles account name will not be matched",
      "order": 7
    },
    "skip": {
      "type": "integer",
      "title": "Skip",
      "description": "Skip first number of items (0-1000). For iterating over more than a 1000 items please use cursor instead. Example 150",
      "order": 3
    },
    "skip_count": {
      "type": "boolean",
      "title": "Skip Count",
      "description": "If true, total number of items will not be calculated, which speeds up execution time",
      "order": 9
    },
    "sort_by": {
      "type": "string",
      "title": "Sort by",
      "description": "The column to sort the results by. Example id",
      "enum": [
        "id",
        "name",
        "totalLicenses",
        "expiration",
        "accountType",
        "state",
        "createdAt",
        "updatetAt",
        "activeLicenses",
        "activeAgents",
        "numberOfSites"
      ],
      "order": 20
    },
    "sort_order": {
      "type": "string",
      "title": "Sort Order",
      "description": "Sort direction. Example asc",
      "enum": [
        "asc",
        "desc"
      ],
      "order": 15
    },
    "states": {
      "type": "string",
      "title": "States",
      "description": "List of states to filter",
      "order": 11
    },
    "total_licenses": {
      "type": "integer",
      "title": "Total Licenses",
      "description": "Filter by total licenses number",
      "order": 18
    },
    "updated_at": {
      "type": "string",
      "title": "Updated at",
      "description": "Timestamp of last update. Example 2018-02-27T04:49:26.257525Z",
      "order": 10
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAccountsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Data",
      "description": "Response data",
      "items": {
        "$ref": "#/definitions/account_data"
      },
      "order": 1
    },
    "pagination": {
      "$ref": "#/definitions/pagination",
      "title": "Pagination",
      "description": "Pagination information",
      "order": 2
    }
  },
  "definitions": {
    "account_data": {
      "type": "object",
      "title": "account_data",
      "properties": {
        "accountType": {
          "type": "string",
          "title": "Account type",
          "order": 7
        },
        "activeAgents": {
          "type": "integer",
          "title": "Active agents number",
          "description": "Total agents in the account",
          "order": 19
        },
        "agentsInCompleteSku": {
          "type": "integer",
          "title": "Agents in complete sku",
          "description": "Number of agents connected to a complete site",
          "order": 20
        },
        "agentsInCoreSku": {
          "type": "integer",
          "title": "Agents in core SKU",
          "description": "Number of agents connected to a core site",
          "order": 2
        },
        "completeSites": {
          "type": "integer",
          "title": "Complete sites",
          "description": "Number of sites in suite Complete",
          "order": 22
        },
        "coreSites": {
          "type": "string",
          "title": "Core sites",
          "description": "Number of sites in suite Core",
          "order": 14
        },
        "createdAt": {
          "type": "string",
          "title": "Created at",
          "description": "Timestamp of account creation",
          "order": 15
        },
        "creator": {
          "type": "string",
          "title": "Creator",
          "description": "The user that created the group",
          "order": 1
        },
        "creatorId": {
          "type": "string",
          "title": "Creator ID",
          "description": "The ID of the user that created the group",
          "order": 9
        },
        "expiration": {
          "type": "string",
          "title": "Expiration",
          "description": "When account should expire, example: 2018-02-27T04:49:26.257525Z",
          "order": 8
        },
        "externalId": {
          "type": "string",
          "title": "Exteral ID",
          "description": "ID of CRM external system",
          "order": 16
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Account ID",
          "order": 17
        },
        "isDefault": {
          "type": "boolean",
          "title": "Is default",
          "order": 21
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 13
        },
        "numberOfSites": {
          "type": "integer",
          "title": "Number of sites",
          "description": "Total number of sites in this account",
          "order": 5
        },
        "skus": {
          "type": "string",
          "title": "Skus",
          "order": 18
        },
        "state": {
          "type": "string",
          "title": "Account state",
          "enum": [
            "active",
            "expired",
            "deleted"
          ],
          "order": 6
        },
        "totalComplete": {
          "type": "integer",
          "title": "Total complete",
          "order": 3
        },
        "totalCore": {
          "type": "integer",
          "title": "Total core",
          "order": 12
        },
        "unlimitedComplete": {
          "type": "boolean",
          "title": "Unlimited complete",
          "order": 4
        },
        "unlimitedCore": {
          "type": "boolean",
          "title": "Unlimited core",
          "order": 23
        },
        "unlimitedExpiration": {
          "type": "boolean",
          "title": "Unlimited expiration",
          "description": "The account does not expire",
          "order": 11
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated at",
          "description": "Timestamp of last update",
          "order": 10
        }
      },
      "required": [
        "externalId"
      ]
    },
    "pagination": {
      "type": "object",
      "title": "pagination",
      "properties": {
        "nextCursor": {
          "type": "string",
          "title": "Next Cursor",
          "description": "Next cursor",
          "order": 2
        },
        "totalItems": {
          "type": "integer",
          "title": "Total Items",
          "description": "Total items",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
