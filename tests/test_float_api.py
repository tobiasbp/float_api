
from pytest import fixture

from float_api import Project
from float_api import People

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

def test_project_get(project_keys):
  """
  Get a single project
  """
  
  # The project ID to test
  project_id = 2502659

  # Get a project by ID
  #project = Project(p_id)

  # Get the project info
  r = Project.get(project_id)

  # Make sure we have a dict
  assert isinstance(r, dict)

  # Make sure we have all project keys
  assert set(project_keys).issubset(r.keys()), "All keys must be in response"

  # Make sure we got the project_id
  assert r['project_id'] == project_id, "project_id must be in response"


def test_project_get_all(project_keys):
  """
  Get a list of projects
  """

  # Get a list of all projects
  r = Project.get()
  
  # Make sure we have a list in the result
  assert isinstance(r, list), "Project list must be a list"
  
  # Make sure all projects have all project keys
  for p in r:
    assert isinstance(p, dict), "Project list entries must be dicts"
    assert set(project_keys).issubset(p.keys()), "All project keys must be in projects"


def test_project_add(project_keys):
  """
  Add a new project
  Get the new person
  Update the new person
  Delete the new person
  """
  
  # The data for the new person
  data = {
    "name": "Demo project",
    "notes": "Created by API for testing"
    }

  # Add a new person
  r = Project.add(data)

  # Make sure we got a dict
  assert isinstance(r, dict), "Add project must return a  dict"

  # Make sure the new project dict has all the project keys
  assert set(project_keys).issubset(r.keys()), "Project keys must be in new project"

  # Name of new project must match in response
  assert r['name'] == data['name'], "New project response must have the name we ordered" 

  
  # Get the newly created project
  r = Project.get(r['project_id'])

  # Make sure we got a dict
  assert isinstance(r, dict), "Get project must return a  dict"

  # Make sure we have all the person keys
  assert set(project_keys).issubset(r.keys()), "Project keys must be in project"

  # Name of new project must match
  assert r['name'] == data['name'], "New Project must have the name we ordered" 


  # FIXME: Put random data in all fields?
  # Set notes in dict of newly created project
  new_notes = "JustTestingNotes"
  r['notes'] = new_notes
  
  # Update the project with new notes
  r = Project.update(r)

  # Make sure we got a dict
  assert isinstance(r, dict), "Updated project must return a  dict"

  # Make sure we have all the project keys
  assert set(project_keys).issubset(r.keys()), "Project keys must be in updated project"

  # Notes of update project must match
  assert r['notes'] == new_notes, "Updated project must have new notes" 

  
  # Delete the project we just created
  r = Project.delete(r['project_id'])
  
  # Makes sure we have a status code
  assert isinstance(r, int), "Deletion must a status code integer"

  # Response must be a 204 on successfull deletion
  assert r == 204, "Successfull deletion must return status code 204"


def test_people_get_all(people_keys):
  """
  Get all people
  """
  
  # Get all people (No ID supplied)
  r = People.get()
  
  for p in r:
    assert isinstance(p, dict), "Person list entries must be dicts"
    assert set(people_keys).issubset(p.keys()), "All people keys must be in people"


def test_people_invalid_id():
  """
  Get an invalid person
  """
  
  r = People.get(1)

  assert isinstance(r, dict)
  
  assert r['status'] == 404, "Invalid people ID should not be found"


def test_people_add(people_keys):
  """
  Add a new person
  Get the new person
  Update the new person
  Delete the new person
  """
  
  # The data for the new person
  data = {
    "name": "Mr. Foo Bar",
    "notes": "Created by API for testing"
    }

  # Add a new person
  r = People.add(data)

  # Make sure we got a dict
  assert isinstance(r, dict), "Add person must return a  dict"

  # Make sure the new person dict has all the people keys
  assert set(people_keys).issubset(r.keys()), "People keys must be in new people"

  # Name of new user must match in response
  assert r['name'] == data['name'], "New person response must have the name we ordered" 


  # Get the newly created user
  r = People.get(r['people_id'])

  # Make sure we got a dict
  assert isinstance(r, dict), "Get person must return a  dict"

  # Make sure we have all the person keys
  assert set(people_keys).issubset(r.keys()), "People keys must be in people"

  # Name of new user must match
  assert r['name'] == data['name'], "New person must have the name we ordered" 


  # FIXME: Put random data in all fields?
  # Set job_title in dict of newly created user
  new_title = "JustTestingTitle"
  r['job_title'] = new_title
  
  # Update the user with new title
  r = People.update(r)

  # Make sure we got a dict
  assert isinstance(r, dict), "Updated person must return a  dict"

  # Make sure we have all the person keys
  assert set(people_keys).issubset(r.keys()), "People keys must be in updated people"

  # Name of new user must match
  assert r['job_title'] == new_title, "Updated person must have new job_title" 


  # Delete the user we just created
  r = People.delete(r['people_id'])
  
  # Makes sure we have a status code
  assert isinstance(r, int), "Deletion must a status code integer"

  # Reponse must be a 204 on successfull deletion
  assert r == 204, "Successfull deletion must return status code 204"

