import os

# Import the API
from float_api import FloatAPI

# Get access token from environment variable
FLOAT_ACCESS_TOKEN = os.environ.get('FLOAT_ACCESS_TOKEN', None)

# Create an API object
api = FloatAPI(FLOAT_ACCESS_TOKEN)

print("All people:")
for p in api.get_all_people():
  print(p)

print("All tasks:")
for t in api.get_all_tasks():
  print(t)

print("All clients:")
for t in api.get_all_clients():
  print(t)

print("All departments:")
for d in api.get_all_departments():
  print(d)

print("Get accounts:")
for a in api.get_all_accounts():
  print(a)



# Create a project
#project = f.create_project(name='Project FooBar ')

# Delete a project
#result = f.delete_project(project['project_id'])

# Create a client
#client = f.create_client("Client FooBar")

# Delete a client
#result = f.delete_client(client['client_id'])

