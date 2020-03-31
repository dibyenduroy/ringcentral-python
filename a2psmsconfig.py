import os
import sys
import json

def get_config_parser():
    if sys.version_info[0] == 3:
        from configparser import ConfigParser
        return ConfigParser
    else:
        import ConfigParser
        return ConfigParser.ConfigParser


ConfigParser = get_config_parser()
#config = ConfigParser()
#config.read('credentials.ini')

#USERNAME = config.get('Credentials', 'USERNAME')
#EXTENSION = config.get('Credentials', 'EXTENSION')
#PASSWORD = config.get('Credentials', 'PASSWORD')
#APP_KEY = config.get('Credentials', 'APP_KEY')
#APP_SECRET = config.get('Credentials', 'APP_SECRET')
#SERVER = config.get('Credentials', 'SERVER')
#MOBILE = config.get('Credentials', 'MOBILE')

#Sandbox
#USERNAME='+15856234138'
#EXTENSION='101'
#PASSWORD='P@ssw0rd'
#APP_KEY='yDDeslGgQw6NW6dAI5YKew'
#APP_SECRET='_3b0TciuTley-lwyfq6TzghO1IU39lQJ63zge8saIAlA'
#SERVER='https://platform.devtest.ringcentral.com'

#Production
USERNAME='+18883303674'
EXTENSION='101'
PASSWORD='P@ssw0rd'
APP_KEY='PecY7xaOSaSUGkALifVcWQ'
APP_SECRET='2tyIzCYSR4y4NH6fZQHb9A4YQqGPhaTzqjS7-wVbGwng'
SERVER='https://platform.ringcentral.com'
