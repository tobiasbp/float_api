
import os
import requests


# Get access token from environment variable
FLOAT_ACCESS_TOKEN = os.environ.get('FLOAT_ACCESS_TOKEN', None)

# The base URL af all calls to the Float API
#base_url = 'https://api.float.com/v3/{}'

# Throw an error if we did not get the API token 
#class APITokenMissingError(Exception):
#  pass

# Raise an error if we do not have an access token
#if FLOAT_ACCESS_TOKEN == None:
#  raise APIKeyMissingError(
#    "No API key in FLOAT_ACCESS_TOKEN"
#    )


# Create a new requests session
session = requests.Session()
headers = {"Authorization": "Bearer " + FLOAT_ACCESS_TOKEN}


# Import here, since Project needs the session
#from .float_api import Clients
#from .float_api import People
#from .float_api import Project
from .float_api import FloatAPI



