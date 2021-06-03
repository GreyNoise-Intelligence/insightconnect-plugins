# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Input:
    API_KEY = "api_key"
    SSL_VERIFY = "ssl_verify"
    URL = "url"
    USERNAME = "username"
    

class ConnectionSchema(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "api_key": {
      "$ref": "#/definitions/credential_secret_key",
      "title": "API Key",
      "description": "Enter the API key",
      "order": 3
    },
    "ssl_verify": {
      "type": "boolean",
      "title": "SSL Verify",
      "description": "Verify server's certificate",
      "default": false,
      "order": 4
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "Host URL, E.g. https://localhost:8443",
      "order": 1
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Enter the API username",
      "order": 2
    }
  },
  "required": [
    "api_key",
    "ssl_verify",
    "url",
    "username"
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