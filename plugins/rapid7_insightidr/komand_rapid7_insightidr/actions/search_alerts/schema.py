# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Allows the user to search for alerts that match the given criteria"


class Input:
    AGGREGATES = "aggregates"
    END_TIME = "end_time"
    FIELD_IDS = "field_ids"
    INDEX = "index"
    LEQL = "leql"
    RRNS_ONLY = "rrns_only"
    SIZE = "size"
    SORTS = "sorts"
    START_TIME = "start_time"
    TERMS = "terms"


class Output:
    ALERTS = "alerts"
    METADATA = "metadata"
    RRNS = "rrns"


class SearchAlertsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "aggregates": {
      "type": "array",
      "title": "Aggregates",
      "description": "Aggregations to apply for all matching results",
      "items": {
        "$ref": "#/definitions/aggregate_object"
      },
      "order": 7
    },
    "end_time": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "End Time",
      "description": "An optional-ISO formatted timestamp, where only investigations whose createTime is before this date will be returned, if provided a start time will also need provided. If no times are provided a default of 6 months will be used",
      "order": 2
    },
    "field_ids": {
      "type": "array",
      "title": "Field IDs",
      "description": "Additional fields to include for each alert. No additional fields are included if field_ids is empty",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "index": {
      "type": "integer",
      "title": "Index",
      "description": "Zero-based index of the page to retrieve, where value must be greater than or equal to 0",
      "default": 0,
      "order": 9
    },
    "leql": {
      "type": "string",
      "title": "LEQL",
      "description": "The LEQL 'WHERE' clause to match against",
      "order": 3
    },
    "rrns_only": {
      "type": "boolean",
      "title": "RRNs Only",
      "description": "Indicates whether the response returns only the alert Rapid7 Resource Names (RRNs) or the alert RRNs and the alert details. If rrns_only is set to TRUE, the response returns the RRNs only. If rrns_only is set to FALSE or is unspecified, the response returns the RRNs and the alert details",
      "default": false,
      "order": 10
    },
    "size": {
      "type": "integer",
      "title": "Size",
      "description": "Amount of data for a page to retrieve, where its value must be greater than 0 or less than or equal to 100",
      "default": 100,
      "order": 8
    },
    "sorts": {
      "type": "array",
      "title": "Sorts",
      "description": "The sort order to apply to the matching results., where possible field values are RRN, PRIORITY, CREATED TIME, and order values are ASCENDING_NULLS_LAST, ASCENDING_NULLS_FIRST, DESCENDING_NULLS_LAST, DESCENDING_NULLS_FIRST",
      "items": {
        "$ref": "#/definitions/sort_object"
      },
      "order": 5
    },
    "start_time": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Start Time",
      "description": "An optional ISO-formatted timestamp, where only investigations whose createTime is after this date will be returned, if provided an end time will also need provided. If no times are provided a default of 6 months will be used",
      "order": 1
    },
    "terms": {
      "type": "array",
      "title": "Terms",
      "description": "The search terms to match against",
      "items": {
        "$ref": "#/definitions/terms_object"
      },
      "order": 4
    }
  },
  "definitions": {
    "terms_object": {
      "type": "object",
      "title": "terms_object",
      "properties": {
        "field_ids": {
          "type": "array",
          "title": "Field IDs",
          "description": "The identifier of the field for the values to match against.",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "operator": {
          "type": "string",
          "title": "Operator",
          "description": "The search operator to apply.",
          "default": "EQUALS",
          "enum": [
            "NOT_SET",
            "EQUALS",
            "NOT_EQUALS",
            "CONTAINS"
          ],
          "order": 2
        },
        "terms": {
          "title": "Terms",
          "description": "The value for the field to match against. Values are separated by an OR operator.",
          "order": 3
        }
      },
      "required": [
        "terms"
      ]
    },
    "sort_object": {
      "type": "object",
      "title": "sort_object",
      "properties": {
        "field_id": {
          "type": "string",
          "title": "Field ID",
          "description": "The field to aggregate on.",
          "order": 1
        },
        "order": {
          "type": "string",
          "title": "Order",
          "description": "The sort order for the fields.",
          "enum": [
            "ASCENDING_NULLS_LAST",
            "ASCENDING_NULLS_FIRST",
            "DESCENDING_NULLS_LAST",
            "DESCENDING_NULLS_FIRST"
          ],
          "order": 2
        }
      },
      "required": [
        "field_id",
        "order"
      ]
    },
    "aggregate_object": {
      "type": "object",
      "title": "aggregate_object",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The identifier of the aggregation, which you specify. Identifiers should be unique and are included in the response.",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of aggregate.",
          "default": "MEDIAN",
          "enum": [
            "BUCKET",
            "MEDIAN"
          ],
          "order": 2
        },
        "fields": {
          "type": "array",
          "title": "Fields",
          "description": "The field identifiers to aggregate by.",
          "items": {
            "$ref": "#/definitions/field_object"
          },
          "order": 3
        },
        "count_order": {
          "type": "string",
          "title": "Count order",
          "description": "TThe sort order for the count.",
          "enum": [
            "ASCENDING_NULLS_LAST",
            "ASCENDING_NULLS_FIRST",
            "DESCENDING_NULLS_LAST",
            "DESCENDING_NULLS_FIRST"
          ],
          "order": 4
        }
      },
      "required": [
        "count_order",
        "fields",
        "name"
      ]
    },
    "field_object": {
      "type": "object",
      "title": "field_object",
      "properties": {
        "field_id": {
          "type": "string",
          "title": "Field ID",
          "description": "The field to aggregate on.",
          "order": 1
        },
        "interval": {
          "type": "string",
          "title": "Interval",
          "description": "For fields that support histograms (such as number and date fields), the interval for each bucket. For date fields, the interval is interpreted as the number of seconds.",
          "order": 2
        },
        "order": {
          "type": "string",
          "title": "Order",
          "description": "The sort order for the fields.",
          "enum": [
            "ASCENDING_NULLS_LAST",
            "ASCENDING_NULLS_FIRST",
            "DESCENDING_NULLS_LAST",
            "DESCENDING_NULLS_FIRST"
          ],
          "order": 3
        }
      },
      "required": [
        "field_id",
        "order"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchAlertsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alerts": {
      "type": "array",
      "title": "Alerts",
      "description": "A list of found alerts",
      "items": {
        "$ref": "#/definitions/alert_object"
      },
      "order": 1
    },
    "metadata": {
      "$ref": "#/definitions/investigation_metadata",
      "title": "Metadata",
      "description": "The pagination parameters used to generate this page result",
      "order": 3
    },
    "rrns": {
      "type": "array",
      "title": "RRNs",
      "description": "A list of the rrns for the found alerts",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  },
  "required": [
    "metadata"
  ],
  "definitions": {
    "alert_object": {
      "type": "object",
      "title": "alert_object",
      "properties": {
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The unique identifier for this alert.",
          "order": 1
        },
        "version": {
          "type": "integer",
          "title": "Version",
          "description": "The version of the alert.",
          "order": 2
        },
        "created_at": {
          "type": "string",
          "title": "Created at",
          "description": "The timestamp when InsightIDR finished creating the alert in the Alerts experience.",
          "order": 3
        },
        "updated_at": {
          "type": "string",
          "title": "Updated at",
          "description": "The timestamp when the alert was last updated in InsightIDR.",
          "order": 4
        },
        "alerted_at": {
          "type": "string",
          "title": "Alerted at",
          "description": "The timestamp associated with the underlying event or evidence that InsightIDR detected in the source system.",
          "order": 5
        },
        "ingested_at": {
          "type": "string",
          "title": "Ingested at",
          "description": "The timestamp when the event or evidence from the source system was received by the Alerts experience in InsightIDR.",
          "order": 6
        },
        "external_source": {
          "type": "string",
          "title": "External Source",
          "description": "The source of the alert.",
          "order": 7
        },
        "external_id": {
          "type": "string",
          "title": "External ID",
          "description": "The identifier of the alert in the system, identified by external_source.",
          "order": 8
        },
        "organization": {
          "$ref": "#/definitions/organization_object",
          "title": "organization",
          "description": "The details of the organization that the alert belongs to.",
          "order": 9
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "The description of the alert.",
          "order": 10
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The type of alert.",
          "order": 11
        },
        "rule": {
          "$ref": "#/definitions/rule_object",
          "title": "Rule",
          "description": "The details about the alert's detection rule.",
          "order": 12
        },
        "rule_matching_keys": {
          "type": "array",
          "title": "Rule Matching Keys",
          "description": "The keys and values used when matching detection rule logic.",
          "items": {
            "type": "object"
          },
          "order": 13
        },
        "rule_keys_of_interest": {
          "type": "array",
          "title": "Rule Keys of Interest",
          "description": "The keys and values used when matching detection rule logic.",
          "items": {
            "type": "object"
          },
          "order": 14
        },
        "responsibility": {
          "type": "string",
          "title": "Responsibility",
          "description": "Indicates the party responsible for the alert.",
          "enum": [
            "UNMAPPED",
            "CUSTOMER",
            "MDR"
          ],
          "order": 15
        },
        "monitored": {
          "type": "boolean",
          "title": "Monitored",
          "description": "Indicates whether monitoring for the organization was active at the time of the alert.",
          "order": 16
        },
        "assignee": {
          "$ref": "#/definitions/assignee_object",
          "title": "Assignee",
          "description": "The user assigned to the alert.",
          "order": 17
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "The priority of the alert.",
          "enum": [
            "UNMAPPED",
            "INFO",
            "LOW",
            "MEDIUM",
            "HIGH",
            "CRITICAL"
          ],
          "order": 18
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the alert.",
          "enum": [
            "UNMAPPED",
            "OPEN",
            "INVESTIGATING",
            "WAITING",
            "CLOSED"
          ],
          "order": 19
        },
        "status_transitions": {
          "$ref": "#/definitions/status_transitions_object",
          "title": "Status Transitions",
          "description": "Information about when the alert status was changed.",
          "order": 20
        },
        "disposition": {
          "type": "string",
          "title": "Disposition",
          "description": "The disposition of the alert.",
          "enum": [
            "UNMAPPED",
            "UNDECIDED",
            "MALICIOUS",
            "BENIGN",
            "UNKNOWN",
            "NOT_APPLICABLE"
          ],
          "order": 21
        },
        "investigation_rrn": {
          "type": "string",
          "title": "Investigation RRN",
          "description": "The RRN of the investigation that the alert is part of.",
          "order": 22
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "The tags applied to the alert.",
          "items": {
            "type": "string"
          },
          "order": 23
        },
        "permissions": {
          "$ref": "#/definitions/permissions_object",
          "title": "Permissions",
          "description": "The permissions the current caller has for the alert.",
          "order": 24
        },
        "fields": {
          "type": "array",
          "title": "Fields",
          "description": "Additional fields specified in the request.",
          "items": {
            "type": "object"
          },
          "order": 25
        }
      }
    },
    "organization_object": {
      "type": "object",
      "title": "organization_object",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The unique identifier of the organization.",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The display name of the organization.",
          "order": 2
        },
        "region": {
          "type": "string",
          "title": "Region",
          "description": "The region that the organization is assigned to.",
          "order": 3
        },
        "product_token": {
          "type": "string",
          "title": "Product Token",
          "description": "The Platform productToken associated with the organization's product.",
          "order": 4
        },
        "customer_id": {
          "type": "string",
          "title": "Customer ID",
          "description": "The unique identifier of the customer.",
          "order": 5
        },
        "customer_name": {
          "type": "string",
          "title": "Customer Name",
          "description": "The display name of the customer.",
          "order": 6
        },
        "customer_code": {
          "type": "string",
          "title": "Customer Code",
          "description": "The customer code for the organization.",
          "order": 7
        },
        "customer_group": {
          "type": "string",
          "title": "Customer Group",
          "description": "The customer group responsible for the organization.",
          "order": 8
        },
        "flags": {
          "type": "array",
          "title": "Flags",
          "description": "The flags associated with the organization.",
          "items": {
            "type": "string"
          },
          "order": 9
        }
      }
    },
    "rule_object": {
      "type": "object",
      "title": "rule_object",
      "properties": {
        "rrn": {
          "type": "string",
          "title": "RRN",
          "description": "The unique identifier of the detection rule.",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The display name for the detection rule.",
          "order": 2
        },
        "mitre_tcodes": {
          "type": "array",
          "title": "Mitre Tcodes",
          "description": "The mitreTCodes associated with the detection rule.",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "version_rrn": {
          "type": "string",
          "title": "Version RRN",
          "description": "The version RRN of the detection rule.",
          "order": 4
        }
      }
    },
    "assignee_object": {
      "type": "object",
      "title": "assignee_object",
      "properties": {
        "at": {
          "type": "string",
          "title": "At",
          "description": "The timestamp when the user was assigned.",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The unique identifier of the user.",
          "order": 2
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email address of the user.",
          "order": 3
        },
        "first_name": {
          "type": "string",
          "title": "First Name",
          "description": "The displayed first name of the user.",
          "order": 4
        },
        "last_name": {
          "type": "string",
          "title": "Last Name",
          "description": "The displayed last name of the user.",
          "order": 5
        }
      }
    },
    "status_transitions_object": {
      "type": "object",
      "title": "status_transitions_object",
      "properties": {
        "seconds_to_first_investigating": {
          "type": "integer",
          "title": "Seconds to first investigating",
          "description": "The number of seconds between when the alert was created and when the alert moved to the INVESTIGATING status, or when it moved directly to the CLOSED status.",
          "order": 1
        },
        "seconds_to_first_closed": {
          "type": "integer",
          "title": "Seconds to first closed",
          "description": "The number of seconds between when the alert was created and when the alert moved to the CLOSED status.",
          "order": 2
        }
      }
    },
    "permissions_object": {
      "type": "object",
      "title": "permissions_object",
      "properties": {
        "canEdit": {
          "type": "boolean",
          "title": "Can edit",
          "description": "Indicates whether the current caller can edit the alert.",
          "order": 1
        }
      }
    },
    "investigation_metadata": {
      "type": "object",
      "title": "investigation_metadata",
      "properties": {
        "index": {
          "type": "integer",
          "title": "Index",
          "description": "The zero-based index of the page retrieved",
          "order": 1
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "The size of the page requested",
          "order": 2
        },
        "total_data": {
          "type": "integer",
          "title": "Total Data",
          "description": "The total number of results available with the given filter parameters",
          "order": 3
        },
        "total_pages": {
          "type": "integer",
          "title": "Total Pages",
          "description": "The total number of pages available with the given filter parameters",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)