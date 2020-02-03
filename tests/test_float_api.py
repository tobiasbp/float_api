
from pytest import fixture

import os
import sys

#from float_api import Clients
#from float_api import People
#from float_api import Project
from float_api import FloatAPI

# Get access token from environment variable
FLOAT_ACCESS_TOKEN = os.environ.get('FLOAT_ACCESS_TOKEN', None)

@fixture
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


@fixture
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

@fixture
def project_tag_keys():
  return [
    'tag_name'
    'project_id'
    ]

@fixture
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

@fixture
def client_keys():
  return [
    'name',
    'client_id'
    ]


#@fixture
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




api = FloatAPI(FLOAT_ACCESS_TOKEN)

def test_get_all():

  functions = [
    (api.get_all_accounts, account_keys()),
    (api.get_all_clients, client_keys()),
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


def test_create_get_delete():

  functions = [
    (api.create_client, api.delete_client, api.get_client, client_keys(), 'client_id'),
    (api.create_person, api.delete_person, api.get_person, people_keys(), 'people_id'),
    (api.create_project, api.delete_project, api.get_project, project_keys(), 'project_id'),
    ]
  
  for f_create, f_delete, f_get, keys, o_id in functions:
    
    # Create object
    r = f_create(name='TestDataFromAPI 1')
    
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


