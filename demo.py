#!/usr/bin/env python3

import os
from datetime import date
from datetime import timedelta

# Import the API
from float_api import FloatAPI

# Get access token from environment variable
FLOAT_ACCESS_TOKEN = os.environ.get('FLOAT_ACCESS_TOKEN', None)

# Create an API object
api = FloatAPI(FLOAT_ACCESS_TOKEN, 'my_api_demo', 'me@example.org')


# Today
start_date = date.today().isoformat()

# 30 days in the future
end_date = (date.today() + timedelta(days=30)).isoformat()


print("\nPeople:")
for p in api.get_all_people(fields='name,people_id'):
  print(p)

print("\nPeople reports:")
for r in api.get_people_reports(start_date, end_date):
  print(r)

print("\nProjects:")
for p in api.get_all_projects(fields='name'):
  print(p)

print("\nProject reports:")
for r in api.get_project_reports(start_date, end_date):
  print(r.keys())

print("\nTasks:")
for t in api.get_all_tasks(start_date=start_date, end_date=end_date):
  print(t)

print("\nAll clients:")
for c in api.get_all_clients():
  print(c)

print("\nAll departments:")
for d in api.get_all_departments():
  print(d)

print("\nAll accounts:")
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
