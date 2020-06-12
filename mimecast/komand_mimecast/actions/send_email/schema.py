# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Send Email"


class Input:
    ATTACHMENTS = "attachments"
    BCC = "bcc"
    CC = "cc"
    EXTRA_HEADERS = "extra_headers"
    FROM = "from"
    HTML_BODY = "html_body"
    PLAIN_BODY = "plain_body"
    SUBJECT = "subject"
    TO = "to"
    

class Output:
    MESSAGE_DATE_HEADER = "message_date_header"
    MESSAGE_ID = "message_id"
    

class SendEmailInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "attachments": {
      "type": "array",
      "title": "Attachments",
      "description": "An attachment object describing any attachments on the message",
      "items": {
        "$ref": "#/definitions/attachments"
      },
      "order": 4
    },
    "bcc": {
      "type": "array",
      "title": "BCC",
      "description": "An array of recipient objects describing the \\"bcc\\" recipient(s) of the message",
      "items": {
        "$ref": "#/definitions/email_address"
      },
      "order": 9
    },
    "cc": {
      "type": "array",
      "title": "CC",
      "description": "An array of recipient objects describing the \\"cc\\" recipient(s) of the message",
      "items": {
        "$ref": "#/definitions/email_address"
      },
      "order": 6
    },
    "extra_headers": {
      "type": "array",
      "title": "Extra Headers",
      "description": "An array of header objects describing any custom message headers to be included on the message",
      "items": {
        "$ref": "#/definitions/extra_headers"
      },
      "order": 8
    },
    "from": {
      "$ref": "#/definitions/email_address",
      "title": "From",
      "description": "An object describing the sender of the message. If not included, the details of the authorized user are used",
      "order": 3
    },
    "html_body": {
      "$ref": "#/definitions/html_body",
      "title": "Html Body",
      "description": "A body object describing the html body of the message",
      "order": 5
    },
    "plain_body": {
      "$ref": "#/definitions/html_body",
      "title": "Plain Body",
      "description": "A body object describing the plain text body of the message",
      "order": 7
    },
    "subject": {
      "type": "string",
      "title": "Subject",
      "description": "The message subject",
      "order": 2
    },
    "to": {
      "type": "array",
      "title": "To",
      "description": "An array of recipient objects describing the \\"to\\" recipient(s) of the message",
      "items": {
        "$ref": "#/definitions/email_address"
      },
      "order": 1
    }
  },
  "required": [
    "subject",
    "to"
  ],
  "definitions": {
    "attachments": {
      "type": "object",
      "title": "attachments",
      "properties": {
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "The file name to set for the attachment. If not set the API will automatically set the file name to \\"Mail Attachment\\" without a file extension",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The Mimecast ID of a file that has been previously uploaded to Mimecast using the file_upload action",
          "order": 1
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "The size of the message attachment",
          "order": 2
        }
      },
      "required": [
        "id",
        "size"
      ]
    },
    "email_address": {
      "type": "object",
      "title": "email_address",
      "properties": {
        "displayableName": {
          "type": "string",
          "title": "Displayable Name",
          "description": "A display name, if available",
          "order": 2
        },
        "emailAddress": {
          "type": "string",
          "title": "Email Address",
          "description": "An email address",
          "order": 1
        }
      }
    },
    "extra_headers": {
      "type": "object",
      "title": "extra_headers",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 2
        }
      }
    },
    "html_body": {
      "type": "object",
      "title": "html_body",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "The content of the message body as a string",
          "order": 1
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The Mimecast ID of a body part that has been previously uploaded to Mimecast using the /api/file/file-upload function",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SendEmailOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message_date_header": {
      "type": "string",
      "title": "Message Date Header",
      "description": "The date that the message was sent via the API",
      "order": 2
    },
    "message_id": {
      "type": "string",
      "title": "Message ID",
      "description": "The internet message id that the API automatically generates for the message",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)