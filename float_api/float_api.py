import requests
# Import the requests session
#from . import session
#from . import headers
#from . import base_url

class ParameterMissingError(Exception):
  pass

class FloatAPI():


  def __init__(self, access_token):

    # The session to use for all requests
    self.session = requests.Session()

    # Headers to send with every request
    self.headers = {"Authorization": "Bearer " + access_token}

    # The base URL af all calls to the Float API
    self.base_url = 'https://api.float.com/v3/{}'


  def _delete(self, path):
    """
    Args:
      path: The string added to the base URL
    """

    # Build the URL
    url = self.base_url.format(path)

    # Perform request
    r = self.session.delete(url, headers=self.headers)

    # Return data if request was a success.
    # Return empty dict otherwise
    if r.status_code == 204:
      return True
    else:
      return False


  def _get(self, path, error_object):
    """
    Args:
      path: The string added to the base URL
      error_object: The object to return if status code is not 200
    """

    # Build the URL
    url = self.base_url.format(path)

    # Perform request
    r = self.session.get(url, headers=self.headers)

    # Return data if request was a success.
    # Return empty dict otherwise
    if r.status_code == 200:
      return r.json()
    else:
      return error_object


  def _post(self, path, data):
    """
    Args:
      path: The string added to the base URL
      data: The data to post
    """

    # Build the URL
    url = self.base_url.format(path)

    # Post
    r = self.session.post(url, data=data, headers=self.headers)

    # Return data if request was a success.
    # Return empty dict otherwise
    if r.status_code == 201:
      return r.json()
    else:
      return {}


  def _patch(self, path, data):
    """
    Args:
      path: The string added to the base URL
      data: The data to post
    """

    # Build the URL
    url = self.base_url.format(path)

    # Post
    r = self.session.update(url, data=data, headers=self.headers)

    # Return data if request was a success.
    # Return empty dict otherwise
    if r.status_code == 200:
      return r.json()
    else:
      return {}


  ## GET ##
  
  def get_account(self, account_id):

    raise NotImplementedError('Not possible with API')


  def get_client(self, client_id):

    return self._get('clients/{}'.format(client_id), {})


  def get_person(self, people_id):

    return self._get('people/{}'.format(people_id), {})


  def get_project(self, project_id):

    return self._get('projects/{}'.format(project_id), {})


  def get_task(self, task_id):

    return self._get('tasks/{}'.format(task_id), {})


  ## GET ALL ##

  def get_all_accounts(self):
    """
    Get all Float accounts
    """
    return self._get('accounts', [])


  def get_all_clients(self):
    """
    Get all Float clients
    """
    return self._get('clients', [])


  def get_all_people(self):
    """
    Get all Float people
    """
    return self._get('people', [])


  def get_all_projects(self):
    """
    Get all Float clients
    """
    return self._get('projects', [])


  def get_all_tasks(self):
    """
    Get all Float tasks
    """
    return self._get('tasks', [])


  ## CREATE ##

  def create_account(self, **kwargs):

    raise NotImplementedError('Not possible with API')


  def create_client(self, **kwargs):

    if 'name' not in kwargs.keys():
      raise KeyError('Missing required key \'name\'')

    return self._post('clients', kwargs)


  def create_person(self, **kwargs):

    if 'name' not in kwargs.keys():
      raise KeyError('Missing required key \'name\'')
    
    return self._post('people', kwargs)


  def create_project(self, **kwargs):

    if 'name' not in kwargs.keys():
      raise KeyError('Missing required key \'name\'')

    return self._post('projects', kwargs)


  ## UPDATE ##
  
  def update_account(self, **kwargs):

    raise NotImplementedError('Not possible with API')


  def update_client(self, **kwargs):

    if 'client_id' not in kwargs.keys():
      raise KeyError('Missing required key \'client_id\'')

    return self._patch('clients/{}'.format(kwargs['client_id']))


  def update_person(self, **kwargs):

    if 'people_id' not in kwargs.keys():
      raise KeyError('Missing required key \'people_id\'')

    return self._patch('people/{}'.format(kwargs['people_id']))


  def update_project(self, **kwargs):

    if 'project_id' not in kwargs.keys():
      raise KeyError('Missing required key \'project_id\'')

    return self._patch('projects/{}'.format(kwargs['project_id']))


  def update_task(self, **kwargs):

    if 'task_id' not in kwargs.keys():
      raise KeyError('Missing required key \'task_id\'')

    return self._patch('tasks/{}'.format(kwargs['task_id']))


  ## DELETE ##
  
  def delete_account(self, account_id):

    raise NotImplementedError('Not possible with API')


  def delete_client(self, client_id):

    return self._delete('clients/{}'.format(client_id))


  def delete_person(self, person_id):

    return self._delete('people/{}'.format(person_id))


  def delete_project(self, project_id):

    return self._delete('projects/{}'.format(project_id))
