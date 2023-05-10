# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a line plot with an X/Y axis"


class Input:
    COLOR_PALETTE = "color_palette"
    CSV_DATA = "csv_data"
    HUE = "hue"
    MARGIN_STYLE = "margin_style"
    X_VALUE = "x_value"
    Y_VALUE = "y_value"
    

class Output:
    CSV = "csv"
    PLOT = "plot"
    

class CreateLinePlotInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "color_palette": {
      "type": "string",
      "title": "Color Palette",
      "description": "Color palette of the plot",
      "default": "dark",
      "enum": [
        "deep",
        "muted",
        "bright",
        "pastel",
        "dark",
        "colorblind"
      ],
      "order": 5
    },
    "csv_data": {
      "type": "string",
      "title": "CSV Data",
      "displayType": "bytes",
      "description": "Base64 encoded CSV data from which to create the plot",
      "format": "bytes",
      "order": 1
    },
    "hue": {
      "type": "string",
      "title": "Hue",
      "description": "Column by which to provide data segmentation (labels)",
      "order": 4
    },
    "margin_style": {
      "type": "string",
      "title": "Margin Style",
      "description": "Style of the margin of the plot",
      "default": "dark",
      "enum": [
        "darkgrid",
        "whitegrid",
        "dark",
        "white",
        "ticks"
      ],
      "order": 6
    },
    "x_value": {
      "type": "string",
      "title": "X Value",
      "description": "Column containing values for the X-axis of the plot",
      "order": 2
    },
    "y_value": {
      "type": "string",
      "title": "Y Value",
      "description": "Column containing values for the Y-axis of the plot",
      "order": 3
    }
  },
  "required": [
    "color_palette",
    "csv_data",
    "margin_style",
    "x_value",
    "y_value"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateLinePlotOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "csv": {
      "type": "string",
      "title": "CSV",
      "displayType": "bytes",
      "description": "Base64 encoded CSV data used to generate the plot",
      "format": "bytes",
      "order": 1
    },
    "plot": {
      "type": "string",
      "title": "Plot",
      "displayType": "bytes",
      "description": "Base64 encoded PNG plot data (can be attached to an email)",
      "format": "bytes",
      "order": 2
    }
  },
  "required": [
    "csv",
    "plot"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
