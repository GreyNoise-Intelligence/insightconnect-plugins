# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Archive sensor"


class Input:
    ARGUMENT = "argument"
    SENSOR_IDS = "sensor_ids"


class Output:
    ARCHIVE_SENSOR_RESPONSE = "archive_sensor_response"


class ArchiveSensorInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "argument": {
      "type": "string",
      "title": "Argument",
      "description": "The reason for archiving the sensor or sensors",
      "order": 2
    },
    "sensor_ids": {
      "type": "array",
      "title": "Sensor IDS",
      "description": "The unique identifier of the machine(s) you wish to perform the operation on",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "argument",
    "sensor_ids"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ArchiveSensorOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "archive_sensor_response": {
      "$ref": "#/definitions/archiveSensorResponse",
      "title": "Archive Sensor Response",
      "description": "Archive sensor response",
      "order": 1
    }
  },
  "required": [
    "archive_sensor_response"
  ],
  "definitions": {
    "archiveSensorResponse": {
      "type": "object",
      "title": "archiveSensorResponse",
      "properties": {
        "batchId": {
          "type": "integer",
          "title": "Batch ID",
          "description": "The ID for the operation. You may need this number for other operations",
          "order": 1
        },
        "actionType": {
          "type": "string",
          "title": "Action Type",
          "description": "The action taken on the sensor",
          "order": 2
        },
        "actionArguments": {
          "type": "string",
          "title": "Action Arguments",
          "description": "The arguments passed for the operation",
          "order": 3
        },
        "globalStats": {
          "$ref": "#/definitions/globalSensorStats",
          "title": "Global Stats",
          "description": "Collection of items about the operation",
          "order": 4
        },
        "finalState": {
          "type": "boolean",
          "title": "Final State",
          "description": "Indicates whether the sensor is in the state indicated by the operation",
          "order": 5
        },
        "totalNumberOfProbes": {
          "type": "integer",
          "title": "Total Number Of Probes",
          "order": 6
        },
        "initiatorUser": {
          "type": "string",
          "title": "Initiator User",
          "description": "The user name of the user who performed this operation",
          "order": 7
        },
        "startTime": {
          "type": "integer",
          "title": "Start Time",
          "description": "The start time of the operation",
          "order": 8
        },
        "aborterUser": {
          "type": "string",
          "title": "Aborter User",
          "description": "The user name of the user who aborted the operation. This field only exists if the operation was aborted",
          "order": 9
        },
        "abortTime": {
          "type": "integer",
          "title": "Abort Time",
          "description": "The time (in epoch) when the operation was aborted. This field only exists if the operation was aborted",
          "order": 10
        },
        "abortTimeout": {
          "type": "boolean",
          "title": "Abort Timeout",
          "description": "Indicates whether there is a timeout value for timing out the request to abort",
          "order": 11
        },
        "abortHttpStatusCode": {
          "type": "string",
          "title": "Abort HTTP Status Code",
          "description": "The code sent by the server to abort the operation. This field only exists if the operation was aborted",
          "order": 12
        }
      },
      "required": [
        "abortTimeout",
        "actionType",
        "batchId",
        "finalState",
        "globalStats",
        "initiatorUser",
        "startTime",
        "totalNumberOfProbes"
      ]
    },
    "globalSensorStats": {
      "type": "object",
      "title": "globalSensorStats",
      "properties": {
        "stats": {
          "$ref": "#/definitions/sensorStats",
          "title": "sensorStats",
          "description": "Stats",
          "order": 1
        }
      }
    },
    "sensorStats": {
      "type": "object",
      "title": "sensorStats",
      "properties": {
        "failedSending": {
          "type": "integer",
          "title": "Failed Sending",
          "description": "Failed sending",
          "order": 1
        },
        "invalidState": {
          "type": "integer",
          "title": "Invalid State",
          "description": "Invalid state",
          "order": 2
        },
        "probeRemoved": {
          "type": "integer",
          "title": "Probe Removed",
          "description": "Probe removed",
          "order": 3
        },
        "timeoutSending": {
          "type": "integer",
          "title": "Timeout Sending",
          "description": "Timeout sending",
          "order": 4
        },
        "pending": {
          "type": "integer",
          "title": "Pending",
          "description": "Pending",
          "order": 5
        },
        "chunksRequired": {
          "type": "integer",
          "title": "Chunks Required",
          "description": "Chunks required",
          "order": 6
        },
        "msiFileCorrupted": {
          "type": "integer",
          "title": "MSI File Corrupted",
          "description": "MSI file corrupted",
          "order": 7
        },
        "sendingMsi": {
          "type": "integer",
          "title": "Sending MSI",
          "description": "Sending MSI",
          "order": 8
        },
        "newerInstalled": {
          "type": "integer",
          "title": "Newer Installed",
          "description": "Newer installed",
          "order": 9
        },
        "msiSendFail": {
          "type": "integer",
          "title": "MSI Send Fail",
          "description": "MSI Send Fail",
          "order": 10
        },
        "partialResponse": {
          "type": "integer",
          "title": "Partial Response",
          "description": "Partial response",
          "order": 11
        },
        "endedWithSensorTimeout": {
          "type": "integer",
          "title": "Ended With Sensor Timeout",
          "description": "Ended with sensor timeout",
          "order": 12
        },
        "failedSendingToServer": {
          "type": "integer",
          "title": "Failed Sending To Server",
          "description": "Failed sending to server",
          "order": 13
        },
        "gettingChunks": {
          "type": "integer",
          "title": "Getting Chunks",
          "description": "Getting chunks",
          "order": 14
        },
        "aborted": {
          "type": "integer",
          "title": "Aborted",
          "description": "Aborted",
          "order": 15
        },
        "started": {
          "type": "integer",
          "title": "Started",
          "description": "Started",
          "order": 16
        },
        "inProgress": {
          "type": "integer",
          "title": "In Progress",
          "description": "In progress",
          "order": 17
        },
        "disconnected": {
          "type": "integer",
          "title": "Disconnected",
          "description": "Disconnected",
          "order": 18
        },
        "failed": {
          "type": "integer",
          "title": "Failed",
          "description": "Failed",
          "order": 19
        },
        "timeout": {
          "type": "integer",
          "title": "Timeout",
          "description": "Timeout",
          "order": 20
        },
        "endedWithTooManyResults": {
          "type": "integer",
          "title": "Ended With Too Many Results",
          "description": "Ended with too many results",
          "order": 21
        },
        "alreadyUpdated": {
          "type": "integer",
          "title": "Already Updated",
          "description": "Already updated",
          "order": 22
        },
        "endedWithTooManySearches": {
          "type": "integer",
          "title": "Ended With Too Many Searches",
          "description": "Ended with too many searches",
          "order": 23
        },
        "succeeded": {
          "type": "integer",
          "title": "Succeeded",
          "description": "Succeeded",
          "order": 24
        },
        "notSupported": {
          "type": "integer",
          "title": "Not Supported",
          "description": "Not supported",
          "order": 25
        },
        "endedWithUnknownError": {
          "type": "integer",
          "title": "Ended With Unknown Error",
          "description": "Ended with unknown error",
          "order": 26
        },
        "none": {
          "type": "integer",
          "title": "None",
          "description": "None",
          "order": 27
        },
        "primed": {
          "type": "integer",
          "title": "Primed",
          "description": "Primed",
          "order": 28
        },
        "endedWithInvalidParam": {
          "type": "integer",
          "title": "Ended With Invalid Param",
          "description": "Ended with invalid param",
          "order": 29
        },
        "unknownProbe": {
          "type": "integer",
          "title": "Unknown Probe",
          "description": "Unknown probe",
          "order": 30
        },
        "abortTimeout": {
          "type": "integer",
          "title": "Abort Timeout",
          "description": "Abort timeout",
          "order": 31
        },
        "unauthorizedUser": {
          "type": "integer",
          "title": "Unauthorized User",
          "description": "Unauthorized user",
          "order": 32
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
