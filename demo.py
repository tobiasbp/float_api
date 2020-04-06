import os
from datetime import date
from datetime import timedelta

# Import the API
from float_api import FloatAPI

# Get access token from environment variable
FLOAT_ACCESS_TOKEN = os.environ.get('FLOAT_ACCESS_TOKEN', None)

# Create an API object
api = FloatAPI(FLOAT_ACCESS_TOKEN, 'my_api_demo', 'me@example.org')

print("All people:")
for p in api.get_all_people(fields='name,people_id'):
  print(p)

print("All projects:")
for p in api.get_all_projects(fields='name'):
  print(p)

print("All tasks:")
for t in api.get_all_tasks():
  print(t)

print("All clients:")
for c in api.get_all_clients():
  print(c)

print("All departments:")
for d in api.get_all_departments():
  print(d)

print("All accounts:")
for a in api.get_all_accounts():
  print(a)

# Create a project
#project = api.create_project(name='Project FooBar ')
#print(project)

# Delete a project
#result = api.delete_project(project['project_id'])
#print(result)

# Create a client
#client = api.create_client("Client FooBar")
#print(client)

# Delete a client
#result = api.delete_client(client['client_id'])
#print(result)
