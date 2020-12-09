# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve agent details"


class Input:
    AGENT = "agent"
    CASE_SENSITIVE = "case_sensitive"
    

class Output:
    AGENT = "agent"
    

class GetAgentDetailsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Agent to retrieve device information from. Accepts IP address, MAC address, hostname, UUID or agent ID",
      "order": 1
    },
    "case_sensitive": {
      "type": "boolean",
      "title": "Case Sensitive",
      "description": "Looks up the specified Agent in a case-sensitive manner. Setting this to false may result in longer run times and unintended results",
      "default": true,
      "order": 2
    }
  },
  "required": [
    "agent",
    "case_sensitive"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAgentDetailsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "$ref": "#/definitions/agent_data",
      "title": "Agent",
      "description": "Detailed information about agent found",
      "order": 1
    }
  },
  "definitions": {
    "agent_data": {
      "type": "object",
      "title": "agent_data",
      "properties": {
        "accountId": {
          "type": "string",
          "title": "Account ID",
          "description": "A reference to the containing account",
          "order": 20
        },
        "accountName": {
          "type": "string",
          "title": "Account Name",
          "description": "Name of the containing account",
          "order": 13
        },
        "activeDirectory": {
          "type": "object",
          "title": "Active Directory",
          "description": "Active Directory data",
          "order": 17
        },
        "activeThreats": {
          "type": "integer",
          "title": "Active Threats",
          "description": "Current number of active threats",
          "order": 23
        },
        "agentVersion": {
          "type": "string",
          "title": "Agent Version",
          "description": "Agent version",
          "order": 53
        },
        "allowRemoteShell": {
          "type": "boolean",
          "title": "Allow Remote Shell",
          "description": "Agent is capable and policy enabled for remote shell",
          "order": 52
        },
        "appsVulnerabilityStatus": {
          "type": "string",
          "title": "Apps Vulnerability Status",
          "description": "Apps vulnerability status",
          "order": 7
        },
        "computerName": {
          "type": "string",
          "title": "Computer Name",
          "description": "Computer name",
          "order": 43
        },
        "consoleMigrationStatus": {
          "type": "string",
          "title": "Console Migration Status",
          "description": "What step the agent is at in the process of migrating to another console, if any",
          "order": 27
        },
        "coreCount": {
          "type": "integer",
          "title": "Core Count",
          "description": "Number of CPU cores",
          "order": 51
        },
        "cpuCount": {
          "type": "integer",
          "title": "CPU Count",
          "description": "Number of CPUs",
          "order": 48
        },
        "cpuId": {
          "type": "string",
          "title": "CPU ID",
          "description": "CPU model",
          "order": 59
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Created at date",
          "order": 9
        },
        "domain": {
          "type": "string",
          "title": "Domain",
          "description": "Network domain",
          "order": 38
        },
        "encryptedApplications": {
          "type": "boolean",
          "title": "Encrypted Applications",
          "description": "Disk encryption status",
          "order": 36
        },
        "externalId": {
          "type": "string",
          "title": "External ID",
          "description": "External id set by customer",
          "order": 50
        },
        "externalIp": {
          "type": "string",
          "title": "External IP",
          "description": "External IPv4 address",
          "order": 3
        },
        "groupId": {
          "type": "string",
          "title": "Group ID",
          "description": "A reference to the containing network group",
          "order": 11
        },
        "groupIp": {
          "type": "string",
          "title": "Group IP",
          "description": "IP Address subnet",
          "order": 54
        },
        "groupName": {
          "type": "string",
          "title": "Group Name",
          "description": "Name of the containing network group",
          "order": 26
        },
        "groupUpdatedAt": {
          "type": "string",
          "title": "Group Updated At",
          "description": "Date of when the group was last updated",
          "order": 42
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Agent ID",
          "order": 29
        },
        "inRemoteShellSession": {
          "type": "boolean",
          "title": "In Remote Shell Session",
          "description": "Is the Agent in a remote shell session",
          "order": 2
        },
        "infected": {
          "type": "boolean",
          "title": "Infected",
          "description": "Indicates if the Agent has active threats",
          "order": 28
        },
        "installerType": {
          "type": "string",
          "title": "Installer Type",
          "description": "Installer package type (file extension)",
          "order": 24
        },
        "isActive": {
          "type": "boolean",
          "title": "Is Active",
          "description": "Indicates if the agent was recently active",
          "order": 47
        },
        "isDecommissioned": {
          "type": "boolean",
          "title": "Is Decommissioned",
          "description": "Is Agent decommissioned",
          "order": 32
        },
        "isPendingUninstall": {
          "type": "boolean",
          "title": "Is Pending Uninstall",
          "description": "Agent with a pending uninstall request",
          "order": 12
        },
        "isUninstalled": {
          "type": "boolean",
          "title": "Is Uninstalled",
          "description": "Indicates if Agent was removed from the device",
          "order": 44
        },
        "isUpToDate": {
          "type": "boolean",
          "title": "Is Up to Date",
          "description": "Indicates if the agent version is up to date",
          "order": 5
        },
        "lastActiveDate": {
          "type": "string",
          "title": "Last Active Date",
          "description": "Last active date",
          "order": 60
        },
        "lastLoggedInUserName": {
          "type": "string",
          "title": "Last Logged In User Name",
          "description": "Last logged in user name",
          "order": 58
        },
        "licenseKey": {
          "type": "string",
          "title": "License Key",
          "description": "License key",
          "order": 46
        },
        "locationType": {
          "type": "string",
          "title": "Location Type",
          "description": "Reported location type",
          "order": 39
        },
        "locations": {
          "type": "array",
          "title": "Locations",
          "description": "A list of locations reported by the Agent",
          "items": {
            "type": "object"
          },
          "order": 37
        },
        "machineType": {
          "type": "string",
          "title": "Machine Type",
          "description": "Machine type",
          "order": 31
        },
        "mitigationMode": {
          "type": "string",
          "title": "Mitigation Mode",
          "description": "Agent mitigation mode policy",
          "order": 4
        },
        "mitigationModeSuspicious": {
          "type": "string",
          "title": "Mitigation Mode Suspicious",
          "description": "Mitigation mode policy for suspicious activity",
          "order": 56
        },
        "modelName": {
          "type": "string",
          "title": "Model Name",
          "description": "Model name",
          "order": 49
        },
        "networkInterfaces": {
          "type": "array",
          "title": "Network Interfaces",
          "description": "Device's network interfaces",
          "items": {
            "type": "object"
          },
          "order": 18
        },
        "networkStatus": {
          "type": "string",
          "title": "Network Status",
          "description": "Agent's network connectivity status",
          "order": 62
        },
        "osArch": {
          "type": "string",
          "title": "OS Arch",
          "description": "OS Arch",
          "order": 22
        },
        "osName": {
          "type": "string",
          "title": "OS Name",
          "description": "Os name",
          "order": 55
        },
        "osRevision": {
          "type": "string",
          "title": "OS Revision",
          "description": "OS revision",
          "order": 33
        },
        "osStartTime": {
          "type": "string",
          "title": "OS Start Time",
          "description": "Last boot time",
          "order": 16
        },
        "osType": {
          "type": "string",
          "title": "OS Type",
          "description": "OS type",
          "order": 61
        },
        "osUsername": {
          "type": "string",
          "title": "OS Username",
          "description": "Os username",
          "order": 57
        },
        "policyUpdatedAt": {
          "type": "string",
          "title": "Policy Updated At",
          "description": "Date of when the policy was last updated",
          "order": 35
        },
        "rangerStatus": {
          "type": "string",
          "title": "Ranger Status",
          "description": "Is Agent disabled as a Ranger",
          "order": 19
        },
        "rangerVersion": {
          "type": "string",
          "title": "Ranger Version",
          "description": "The version of Ranger",
          "order": 8
        },
        "registeredAt": {
          "type": "string",
          "title": "Registered At",
          "description": "Time of first registration to management console (similar to createdAt)",
          "order": 40
        },
        "scanAbortedAt": {
          "type": "string",
          "title": "Scan Aborted At",
          "description": "Abort time of last scan",
          "order": 6
        },
        "scanFinishedAt": {
          "type": "string",
          "title": "Scan Finished At",
          "description": "Finish time of last scan",
          "order": 1
        },
        "scanStartedAt": {
          "type": "string",
          "title": "Scan Started At",
          "description": "Start time of last scan",
          "order": 34
        },
        "scanStatus": {
          "type": "string",
          "title": "Scan Status",
          "description": "Last scan status",
          "order": 25
        },
        "siteId": {
          "type": "string",
          "title": "Site ID",
          "description": "A reference to the containing site",
          "order": 14
        },
        "siteName": {
          "type": "string",
          "title": "Site Name",
          "description": "Name of the containing site",
          "order": 15
        },
        "threatRebootRequired": {
          "type": "boolean",
          "title": "Threat Reboot Required",
          "description": "Has at least one threat with at least one mitigation action that is pending reboot to succeed",
          "order": 21
        },
        "totalMemory": {
          "type": "integer",
          "title": "Total Memory",
          "description": "Memory size (MB)",
          "order": 41
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated at",
          "description": "Last updated date",
          "order": 30
        },
        "userActionsNeeded": {
          "type": "array",
          "title": "User Actions Needed",
          "description": "A list of pending user actions",
          "items": {
            "type": "string"
          },
          "order": 10
        },
        "uuid": {
          "type": "string",
          "title": "UUID",
          "description": "Agent's universally unique identifier",
          "order": 45
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
