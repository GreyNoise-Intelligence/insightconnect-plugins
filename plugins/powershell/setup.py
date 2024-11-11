# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="powershell-rapid7-plugin",
      version="3.0.6",
      description="[PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-6) is a task-based command-line shell and scripting language from Microsoft that helps system administrators, power-users, and InsightConnect customers rapidly automate tasks that manage operating systems and processes. This plugin runs a PowerShell script on a remote host or locally on an InsightConnect Orchestrator",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_powershell']
      )
