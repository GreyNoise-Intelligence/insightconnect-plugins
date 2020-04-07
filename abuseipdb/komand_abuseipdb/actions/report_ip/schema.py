# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Report an abusive IP address"


class Input:
    CATEGORIES = "categories"
    COMMENT = "comment"
    IP = "ip"
    

class Output:
    ABUSECONFIDENCESCORE = "abuseConfidenceScore"
    IPADDRESS = "ipAddress"
    SUCCESS = "success"
    

class ReportIpInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "categories": {
      "type": "string",
      "title": "Categories",
      "description": "Comma delineated list of category IDs e.g. 10,12,15. Entire list is available at https://www.abuseipdb.com/categories",
      "order": 2
    },
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Describe the type of malicious activity e.g. Brute forcing Wordpress login",
      "order": 3
    },
    "ip": {
      "type": "string",
      "title": "IP Address",
      "description": "IPv4 or IPv6 address to report e.g. 198.51.100.100, ::1",
      "order": 1
    }
  },
  "required": [
    "categories",
    "ip"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ReportIpOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "abuseConfidenceScore": {
      "type": "integer",
      "title": "Abuse Confidence Score",
      "description": "Confidence that reported IP is abusive",
      "order": 2
    },
    "ipAddress": {
      "type": "string",
      "title": "Comment",
      "description": "IP address submitted",
      "order": 1
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Submission success",
      "order": 3
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
