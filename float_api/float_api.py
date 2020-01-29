# Import the requests session
from . import session
from . import headers
from . import base_url

class Clients():
  """
  Clients in Float. The have unique names.
  """

  @staticmethod
  def get(client_id = None):
    """
    Get a single Client entry if client_id is supplied,
    get all Clients otherwise.
    """

    if client_id:
      url = base_url.format('clients/' + str(client_id))
    else:
      url = base_url.format('clients')

    r = session.get(url, headers=headers)

    return r.json()


  @staticmethod
  def add(name):
    """
    Add a client. Only has field name
    """

    # A dictionary to post
    data = {'name': name}
    
    # Build the URL
    url = base_url.format('clients')

    # Post the data
    r = session.post(url, data=data, headers=headers)

    # Return the result 
    return r.json()


  @staticmethod
  def delete(client_id):
    """
    Delete a client by id
    """

    url = base_url.format('clients/' + str(client_id))

    r = session.delete(url, headers=headers)

    return r.status_code


  @staticmethod
  def update(data):
    """
    Update project. Data must include project_id
    """

    # make sure we have a dict
    assert isinstance(data, dict)

    # project_id must be a key in data
    assert 'client_id' in set(data.keys())

    # Build the URL
    url = base_url.format('clients/' + str(data['client_id']))

    # Post the data
    r = session.patch(url, data=data, headers=headers)

    # Return the result 
    return r.json()


class Project():
  """
  Projects in Float
  """

  @staticmethod
  def get(project_id = None):
    """
    Get a single Project entry if project_id supplied,
    get all projects otherwise.
    """

    if project_id:
      url = base_url.format('projects/' + str(project_id))
    else:
      url = base_url.format('projects')

    r = session.get(url, headers=headers)

    return r.json()


  @staticmethod
  def add(data):
    """
    Add a project
    """

    # Data must be a dict
    assert isinstance(data, dict), "New project data must be a dict"

    # Data must include name
    assert 'name' in set(data.keys()), "name not in new project dict"

    # Build the URL
    url = base_url.format('projects')

    # Post the data
    r = session.post(url, data=data, headers=headers)

    # Return the result 
    return r.json()


  @staticmethod
  def delete(project_id):
    """
    Delete a project by id
    """

    url = base_url.format('projects/' + str(project_id))

    r = session.delete(url, headers=headers)

    return r.status_code


  @staticmethod
  def update(data):
    """
    Update project. Data must include project_id
    """

    # make sure we have a dict
    assert isinstance(data, dict)

    # project_id must be a key in data
    assert 'project_id' in set(data.keys())

    # Build the URL
    url = base_url.format('projects/' + str(data['project_id']))

    # Post the data
    r = session.patch(url, data=data, headers=headers)

    # Return the result 
    return r.json()


class People():
  """
  People in Float
  """

  @staticmethod
  def get(people_id = None):
    """
    Get a single People entry if people_id supplied,
    get all people otherwise.
    """

    if people_id:
      url = base_url.format('people/' + str(people_id))
    else:
      url = base_url.format('people')

    r = session.get(url, headers=headers)

    return r.json()


  @staticmethod
  def add(data):
    """
    Add a person
    """

    # Data must be a dict
    assert isinstance(data, dict), "New person data must be a dict"

    # Data must include name
    assert 'name' in set(data.keys()), "name not in new person dict"

    # Build the URL
    url = base_url.format('people')

    # Post the data
    r = session.post(url, data=data, headers=headers)

    # Return the result 
    return r.json()


  @staticmethod
  def delete(people_id):
    """
    Delete a person by id
    """

    url = base_url.format('people/' + str(people_id))

    print(url)
    r = session.delete(url, headers=headers)
    print(r)

    return r.status_code


  @staticmethod
  def update(data):
    """
    Update person. Data must include person_id
    """

    # make sure we have a dict
    assert isinstance(data, dict)

    # people_id must be a key in data
    assert 'people_id' in set(data.keys())

    # Build the URL
    url = base_url.format('people/' + str(data['people_id']))

    # Post the data
    r = session.patch(url, data=data, headers=headers)

    # Return the result 
    return r.json()
