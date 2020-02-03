import os

from float_api import FloatAPI

# Get access token from environment variable
FLOAT_ACCESS_TOKEN = os.environ.get('FLOAT_ACCESS_TOKEN', None)

# Create a 
f = FloatAPI(FLOAT_ACCESS_TOKEN)

print("All people:")
for p in f.get_all_people():
  print(p)

print("All tasks:")
for t in f.get_all_tasks():
  print(t)

print("All clients:")
for t in f.get_all_clients():
  print(t)

# Create a project
#project = f.create_project(name='Project FooBar ')

# Delete a project
#result = f.delete_project(project['project_id'])

# Create a client
#client = f.create_client("Client FooBar")

# Delete a client
#result = f.delete_client(client['client_id'])

