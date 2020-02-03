import os
import random
import string
import sys
from datetime import date

from pytest import fixture
from float_api import FloatAPI

# Get access token from environment variable
FLOAT_ACCESS_TOKEN = os.environ.get('FLOAT_ACCESS_TOKEN', None)

# Create a Float API instance
api = FloatAPI(FLOAT_ACCESS_TOKEN)

def account_keys():
  return [
    'account_id',
    'name',
    'email',
    'account_type',
    'department_filter_id',
    'view_rights',
    'edit_rights',
    'active',
    'created',
    'modified'
    ]

def project_keys():
  return [
    'project_id',
    'name',
    'client_id',
    'color',
    'notes',
    'tags',
    'budget_type',
    'budget_total',
    'default_hourly_rate',
    'non_billable',
    'tentative',
    'active',
    'project_manager',
    'all_pms_schedule',
    'created',
    'modified'
    ]

def project_tag_keys():
  return [
    'tag_name'
    'project_id'
    ]

def people_keys():
  return [
    'people_id',
    'name',
    'email',
    'job_title',
    'department',
    'notes',
    'avatar_file',
    'auto_email',
    'employee_type',
    'work_days_hours',
    'active',
    'people_type_id',
    'tags',
    'start_date',
    'end_date',
    'default_hourly_rate',
    'created',
    'modified'
    ]

def client_keys():
  return [
    'name',
    'client_id'
    ]

def department_keys():
  return [
    'name',
    'department_id'
    ]

def task_keys():
  return [
    'task_id',
    'project_id',
    'start_date',
    'end_date',
    'start_time',
    'hours',
    'people_id',
    'status',
    'priority',
    'name',
    'notes',
    'repeat_state',
    'repeat_end_date',
    'created_by',
    'created',
    'modified_by',
    'modified'
    ]

def random_string(length=32):
  """
  Return a random string of ASCII letters and
  digits of length 'length'
  """
  # The random string
  s = ''
  
  # Add a number of random samples
  for i in range(length):
    s += random.choice(string.ascii_letters + string.digits)
  
  # Return the random string
  return s


# Create, update and delete a client
def test_client():
  
  # Create a client
  client = api.create_client(name=random_string(32))
  assert isinstance(client, dict), "New client is a dict"
  assert set(client_keys()).issubset(client.keys()), "New client has all keys"

  # Update a client
  name = random_string(32)
  client = api.update_client(
    client_id = client['client_id'],
    name = name
    )
  assert isinstance(client, dict), "Updated client is a dict"
  assert set(client_keys()).issubset(client.keys()), "Updated client has all keys"
  assert client['name'] == name, "Name of client is updated"

  # Delete client
  r = api.delete_client(client['client_id'])
  assert r == True, "Deleted client"


# Create, update and delete a task
def test_task():

  # Create a test project
  project = api.create_project(name=random_string(32))
  assert isinstance(project, dict), "New project is a dict"
  assert set(project_keys()).issubset(project.keys()), "New project has all keys"

  # Create a test person
  person = api.create_person(name=random_string(32))
  assert isinstance(person, dict), "New person is a dict"
  assert set(people_keys()).issubset(person.keys()), "New person has all keys"

  # Create a test task
  task = api.create_task(
    project_id = project['project_id'],
    start_date = date.today().isoformat(),
    end_date = date.today().isoformat(),
    hours = 8,
    people_id = person['people_id']
    )
  assert isinstance(task, dict), "New task is a dict"
  assert set(task_keys()).issubset(task.keys()), "New task has all keys"

  # Update notes of test task
  notes = random_string(32)
  task = api.update_task(
    task_id = task['task_id'],
    notes = notes
    )
  assert isinstance(task, dict), "New task is a dict"
  assert set(task_keys()).issubset(task.keys()), "New task has all keys"
  assert task['notes'] == notes, "Notes of task are updated"

  # Delete test task
  r = api.delete_task(task['task_id'])
  assert r == True

  # Delete test person
  r = api.delete_person(person['people_id'])
  assert r == True

  # Delete test project
  r = api.delete_project(project['project_id'])
  assert r == True


# Create, update and delete a person
def test_person():
  
  # Create a person
  person = api.create_person(name=random_string(32))
  assert isinstance(person, dict), "New person is a dict"
  assert set(people_keys()).issubset(person.keys()), "New person has all keys"

  # Update a person
  notes = random_string(32)
  person = api.update_person(
    people_id = person['people_id'],
    notes = notes
    )
  assert isinstance(person, dict), "Updated person is a dict"
  assert set(people_keys()).issubset(person.keys()), "Updated person has all keys"
  assert person['notes'] == notes, "Notes of person are updated"

  # Delete person
  r = api.delete_person(person['people_id'])
  assert r == True, "Deleted person"


# Create, update and delete a project
def test_project():
  
  # Create a project
  project = api.create_project(name=random_string(32))
  assert isinstance(project, dict), "New project is a dict"
  assert set(project_keys()).issubset(project.keys()), "New project has all keys"

  # Update a project
  notes = random_string(32)
  project = api.update_project(
    project_id = project['project_id'],
    notes = notes
    )
  assert isinstance(project, dict), "Updated project is a dict"
  assert set(project_keys()).issubset(project.keys()), "Updated project has all keys"
  assert project['notes'] == notes, "Notes of project are updated"

  # Delete project
  r = api.delete_project(project['project_id'])
  assert r == True, "Deleted project"


# Create, update and delete a department
def test_department():
  
  # Create a department
  department = api.create_department(name=random_string(32))
  assert isinstance(department, dict), "New department is a dict"
  assert set(department_keys()).issubset(department.keys()), "New department has all keys"

  # Update a department
  name = random_string(32)
  department = api.update_department(
    department_id = department['department_id'],
    name = name
    )
  assert isinstance(department, dict), "Updated department is a dict"
  assert set(department_keys()).issubset(department.keys()), "Updated department has all keys"
  assert department['name'] == name, "Name of department is updated"

  # Delete department
  r = api.delete_department(department['department_id'])
  assert r == True, "Deleted department"


# Test get all functions
def test_get_all():

  functions = [
    (api.get_all_accounts, account_keys()),
    (api.get_all_clients, client_keys()),
    (api.get_all_departments, department_keys()),
    (api.get_all_people, people_keys()),
    (api.get_all_projects, project_keys()),
    (api.get_all_tasks, task_keys())
    ]
  
  for func, keys in functions:
    r = func()
    assert isinstance(keys, list), "Keys is a list"
    assert isinstance(r, list), "get all is a list"

    for c in r:
      assert isinstance(c, dict), "Get all list item is a dict"
      assert set(keys).issubset(c.keys()), "Dict has all keys" + str(func)


# Test creation, get'ing and deletion
def test_create_get_delete():

  functions = [
    (api.create_client, api.delete_client, api.get_client, client_keys(), 'client_id'),
    (api.create_person, api.delete_person, api.get_person, people_keys(), 'people_id'),
    (api.create_project, api.delete_project, api.get_project, project_keys(), 'project_id'),
    ]
  
  for f_create, f_delete, f_get, keys, o_id in functions:
    
    # Create object
    r = f_create(name=random_string(32))
    
    assert isinstance(keys, list), "Keys is a list"
    assert isinstance(r, dict), "New object is a list is a list"
    assert set(keys).issubset(r.keys()), "Dict has all keys" + str(f_create)

    # Get object
    created_object = r
    
    # Get the object we just created
    r = f_get(created_object[o_id])
    
    # New object must have all keys
    assert set(keys).issubset(r.keys()), "New objects has all keys" + str(f_get)

    
    # Person: People_type_id is updated after posting, so this fails
    #assert created_object == r, "Get newly created object: {}".format(f_get) 
    
    # FIXME: Update

    # Delete object
    r = f_delete(r[o_id])
    
    assert r == True, "New object deleted" + str(f_delete)

