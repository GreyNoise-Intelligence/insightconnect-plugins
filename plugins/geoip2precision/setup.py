# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='geoip2precision-rapid7-plugin',
      version='1.0.1',
      description='GeoIP2 Precision is a MaxMind service that offers industry-leading IP intelligence data. Users of the GeoIP2 Precision plugin for Rapid7 InsightConnect can use it to geolocate IP addresses',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_geoip2precision']
      )