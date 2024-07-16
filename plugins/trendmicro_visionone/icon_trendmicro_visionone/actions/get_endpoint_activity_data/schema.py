# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Displays results from the Endpoint Activity Data source in a paginated list"


class Input:
    END_DATE_TIME = "end_date_time"
    FIELDS = "fields"
    QUERY_OP = "query_op"
    SELECT = "select"
    START_DATE_TIME = "start_date_time"
    TOP = "top"


class Output:
    ENDPOINT_ACTIVITY_DATA_RESP = "endpoint_activity_data_resp"


class GetEndpointActivityDataInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "end_date_time": {
      "type": "string",
      "title": "End Date Time",
      "description": "Timestamp in ISO 8601 format that indicates the end of the data retrieval time range. If no value is specified, 'endDateTime' defaults to the time the request is made",
      "order": 3
    },
    "fields": {
      "type": "object",
      "title": "Fields",
      "description": "JSON object of fields to query. (uuid, tags, pname, msgUuid, ...)",
      "order": 6
    },
    "query_op": {
      "type": "string",
      "title": "Query Operator",
      "description": "Logical operator to employ in the query. (AND/OR)",
      "default": "or",
      "enum": [
        "or",
        "and"
      ],
      "order": 5
    },
    "select": {
      "type": "array",
      "title": "Select",
      "description": "List of fields to include in the search results. If no fields are specified, the query returns all supported fields",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "start_date_time": {
      "type": "string",
      "title": "Start Date Time",
      "description": "Timestamp in ISO 8601 format that indicates the start of the data retrieval range. If no value is specified, 'startDateTime' defaults to 24 hours before the request is made",
      "order": 2
    },
    "top": {
      "type": "integer",
      "title": "Top",
      "description": "Number of records displayed on a page",
      "enum": [
        50,
        100,
        500,
        1000,
        5000
      ],
      "order": 1
    }
  },
  "required": [
    "fields",
    "query_op",
    "top"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetEndpointActivityDataOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "endpoint_activity_data_resp": {
      "type": "array",
      "title": "Endpoint Activity Data Response",
      "description": "Endpoint Activity Data Response Array",
      "items": {
        "$ref": "#/definitions/endpoint_activity_data_resp"
      },
      "order": 1
    }
  },
  "required": [
    "endpoint_activity_data_resp"
  ],
  "definitions": {
    "endpoint_activity_data_resp": {
      "type": "object",
      "title": "endpoint_activity_data_resp",
      "properties": {
        "dpt": {
          "type": "integer",
          "title": "DPT",
          "description": "Destination port",
          "order": 1
        },
        "dst": {
          "type": "string",
          "title": "DST",
          "description": "Destination IP address",
          "order": 2
        },
        "endpoint_guid": {
          "type": "string",
          "title": "Endpoint GUID",
          "description": "endpoint GUID for identity",
          "order": 3
        },
        "endpoint_host_name": {
          "type": "string",
          "title": "Endpoint Host Name",
          "description": "Hostname of the endpoint on which the event was generated",
          "order": 4
        },
        "endpoint_ip": {
          "type": "array",
          "title": "Endpoint IP",
          "description": "Endpoint IP address list",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "event_id": {
          "type": "string",
          "title": "Event ID",
          "description": "Event ID",
          "order": 6
        },
        "event_sub_id": {
          "type": "integer",
          "title": "Event Sub ID",
          "description": "Event Sub ID",
          "order": 7
        },
        "object_integrity_level": {
          "type": "integer",
          "title": "Object Integrity Level",
          "description": "Object Integrity Level",
          "order": 8
        },
        "object_true_type": {
          "type": "integer",
          "title": "Object True Type",
          "description": "Object True Type",
          "order": 9
        },
        "object_sub_true_type": {
          "type": "integer",
          "title": "Object Sub True Type",
          "description": "Object Sub True Type",
          "order": 10
        },
        "win_event_id": {
          "type": "integer",
          "title": "Win Event ID",
          "description": "Win Event ID",
          "order": 11
        },
        "event_time": {
          "type": "integer",
          "title": "Event Time",
          "description": "Log collect time UTC format",
          "order": 12
        },
        "event_time_d_t": {
          "type": "string",
          "title": "Event Time D T",
          "description": "Log collect time",
          "order": 13
        },
        "host_name": {
          "type": "string",
          "title": "Host Name",
          "description": "Hostname of the endpoint on which the event was generated",
          "order": 14
        },
        "logon_user": {
          "type": "array",
          "title": "Logon User",
          "description": "Logon user name",
          "items": {
            "type": "string"
          },
          "order": 15
        },
        "object_cmd": {
          "type": "string",
          "title": "Object Cmd",
          "description": "Command line entry of target process",
          "order": 16
        },
        "object_file_hash_sha1": {
          "type": "string",
          "title": "Object File Hash SHA1",
          "description": "The SHA1 hash of target process image or target file",
          "order": 17
        },
        "object_file_path": {
          "type": "string",
          "title": "Object File Path",
          "description": "File path location of target process image or target file",
          "order": 18
        },
        "object_host_name": {
          "type": "string",
          "title": "Object Host Name",
          "description": "Server name where Internet event was detected",
          "order": 19
        },
        "object_ip": {
          "type": "string",
          "title": "Object IP",
          "description": "IP address of internet event",
          "order": 20
        },
        "object_ips": {
          "type": "array",
          "title": "Object Ips",
          "description": "IP address list of internet event",
          "items": {
            "type": "string"
          },
          "order": 21
        },
        "object_port": {
          "type": "integer",
          "title": "Object Port",
          "description": "The port number used by internet event",
          "order": 22
        },
        "object_registry_data": {
          "type": "string",
          "title": "Object Registry Data",
          "description": "The registry value data",
          "order": 23
        },
        "object_registry_key_handle": {
          "type": "string",
          "title": "Object Registry Key Handle",
          "description": "The registry key",
          "order": 24
        },
        "object_registry_value": {
          "type": "string",
          "title": "Object Registry Value",
          "description": "Registry value name",
          "order": 25
        },
        "object_signer": {
          "type": "array",
          "title": "Object Signer",
          "description": "Certificate signer of object process or file",
          "items": {
            "type": "string"
          },
          "order": 26
        },
        "object_signer_valid": {
          "type": "array",
          "title": "Object Signer Valid",
          "description": "Validity of certificate signer",
          "items": {
            "type": "boolean"
          },
          "order": 27
        },
        "object_user": {
          "type": "string",
          "title": "Object User",
          "description": "The owner name of target process / The logon user name",
          "order": 28
        },
        "os": {
          "type": "string",
          "title": "OS",
          "description": "SYSTEM",
          "order": 29
        },
        "parent_cmd": {
          "type": "string",
          "title": "Parent Cmd",
          "description": "The command line that parent process",
          "order": 30
        },
        "parent_file_hash_sha1": {
          "type": "string",
          "title": "Parent File Hash SHA1",
          "description": "The SHA1 hash of parent process",
          "order": 31
        },
        "parent_file_path": {
          "type": "string",
          "title": "Parent File Path",
          "description": "The file path location of parent process",
          "order": 32
        },
        "process_cmd": {
          "type": "string",
          "title": "Process Cmd",
          "description": "The command line used to launch this process",
          "order": 33
        },
        "process_file_hash_sha1": {
          "type": "string",
          "title": "Process File Hash SHA1",
          "description": "The process file SHA1",
          "order": 34
        },
        "process_file_path": {
          "type": "string",
          "title": "The process file path",
          "description": "Process File Path",
          "order": 35
        },
        "request": {
          "type": "string",
          "title": "Request",
          "description": "Request URL normally detected by Web Reputation Services",
          "order": 36
        },
        "search_d_l": {
          "type": "string",
          "title": "Search Data Lake",
          "description": "Search data lake",
          "order": 37
        },
        "spt": {
          "type": "integer",
          "title": "SPT",
          "description": "Source port",
          "order": 38
        },
        "src": {
          "type": "string",
          "title": "SRC",
          "description": "Source IP address",
          "order": 39
        },
        "src_file_hash_sha1": {
          "type": "string",
          "title": "Src File Hash SHA1",
          "description": "Source file SHA1",
          "order": 40
        },
        "src_file_path": {
          "type": "string",
          "title": "Src File Path",
          "description": "Src File Path",
          "order": 41
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Detected by Security Analytics Engine filters",
          "items": {
            "type": "string"
          },
          "order": 42
        },
        "uuid": {
          "type": "string",
          "title": "UUID",
          "description": "Log unique identity",
          "order": 43
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
