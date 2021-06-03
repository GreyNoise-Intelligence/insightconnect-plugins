# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    ACCESS_KEY = "access_key"
    HOSTNAME = "hostname"
    SECRET_KEY = "secret_key"
    SSL_VERIFY = "ssl_verify"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "access_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Access Key",
      "order": 1
    },
    "hostname": {
      "type": "string",
      "title": "Hostname",
      "description": "Nessus instance hostname in \\u003cIP Address\\u003e:\\u003cPort\\u003e format",
      "order": 3
    },
    "secret_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "Secret Key",
      "order": 2
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Validate certificate",
      "default": true,
      "order": 4
    }
  },
  "required": [
    "access_key",
    "hostname",
    "secret_key",
    "ssl_verify"
  ],
  "definitions": {
    "credential_secret_key": {
      "id": "credential_secret_key",
      "type": "object",
      "title": "Credential: Secret Key",
      "description": "A shared secret key",
      "properties": {
        "secretKey": {
          "type": "string",
          "title": "Secret Key",
          "displayType": "password",
          "description": "The shared secret key",
          "format": "password"
        }
      },
      "required": [
        "secretKey"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)