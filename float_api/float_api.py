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


  def _get(self, path, error_object, params = None):
    """
    Args:
      path: The string added to the base URL
      error_object: The object to return if status code is not 200
      params: key,value pairs to send in URL
    """

    # Build the URL
    url = self.base_url.format(path)

    # Perform request
    r = self.session.get(url, headers=self.headers, params=params)

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
    print(r.url)
    print(r.status_code)
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
    r = self.session.patch(url, data=data, headers=self.headers)

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


  def get_department(self, department_id):

    return self._get('departments/{}'.format(department_id), {})


  def get_holiday(self, holiday_id):

    r =  self._get('holidays/{}'.format(holiday_id), {})
    #return self._get('holidays/{}'.format(holiday_id), {})
    print(r)
    return r


  def get_milestone(self, milestone_id):

    return self._get('milestones/{}'.format(milestone_id), {})


  def get_person(self, people_id):

    return self._get('people/{}'.format(people_id), {})


  def get_people_reports(self, start_date, end_date, people_id=None):
    """
    Returns a list of reports
    """
    params = {
      'people_id': people_id,
      'start_date': start_date,
      'end_date': end_date
    }

    r = self._get('reports/people', {}, params)

    # Return list in key 'people' of dict
    # or empty list if key not present
    return r.get('people', [])


  def get_project(self, project_id):

    return self._get('projects/{}'.format(project_id), {})


  def get_project_reports(self, start_date, end_date, project_id=None):
    """
    Returns a list of project reports
    """
    # FIXME: I get status_code 422 on these request?
    raise NotImplementedError()
    '''
    params = {
      'project_id': project_id,
      'start_date': start_date,
      'end_date': end_date
    }

    r = self._get('reports/projects', {}, params)

    # Return list in key 'projects' of dict
    # or empty list if key not present
    return r.get('projects', [])
    '''


  def get_task(self, task_id):

    return self._get('tasks/{}'.format(task_id), {})


  def get_timeoff_type(self, timeoff_type_id):

    return self._get('timeoff-types/{}'.format(timeoff_type_id), {})


  ## GET ALL ##

  def get_all_accounts(self):
    """
    Get all Float accounts
    """
    return self._get('accounts', [])


  def get_all_clients(self):

    return self._get('clients', [])


  def get_all_departments(self):

    return self._get('departments', [])


  def get_all_holidays(self):

    return self._get('holidays', [])


  def get_all_milestones(self):

    return self._get('milestones', [])


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


  def get_all_timeoffs(self):

    return self._get('timeoffs', [])


  def get_all_timeoff_types(self):

    return self._get('timeoff-types', [])


  ## CREATE ##

  def create_account(self, **kwargs):

    raise NotImplementedError('Not possible with API')


  def create_client(self, **kwargs):

    if 'name' not in kwargs.keys():
      raise KeyError('Missing required key \'name\'')

    return self._post('clients', kwargs)


  def create_department(self, **kwargs):

    if 'name' not in kwargs.keys():
      raise KeyError('Missing required key \'name\'')

    return self._post('departments', kwargs)


  def create_holiday(self, **kwargs):
    '''
    date must be in the future
    '''
    required_fields = [
      'name',
      'date',
      ]

    for f in required_fields:
      if f not in kwargs.keys():
        raise KeyError('Missing required key \'{}\''.format(f))

    return self._post('holidays', kwargs)


  def create_milestone(self, **kwargs):

    required_fields = [
      'project_id',
      'name',
      'date',
      ]

    for f in required_fields:
      if f not in kwargs.keys():
        raise KeyError('Missing required key \'{}\''.format(f))

    return self._post('milestones', kwargs)


  def create_person(self, **kwargs):

    if 'name' not in kwargs.keys():
      raise KeyError('Missing required key \'name\'')
    
    return self._post('people', kwargs)


  def create_project(self, **kwargs):

    if 'name' not in kwargs.keys():
      raise KeyError('Missing required key \'name\'')

    return self._post('projects', kwargs)


  def create_task(self, **kwargs):

    required_fields = [
      'project_id',
      'start_date',
      'end_date',
      'hours',
      'people_id'
      ]

    for f in required_fields:
      if f not in kwargs.keys():
        raise KeyError('Missing required key \'{}\''.format(f))

    return self._post('tasks', kwargs)


  def create_timeoff(self, **kwargs):

    required_fields = [
      'timeoff_type_id',
      'start_date',
      'end_date',
      'people_ids'
      ]

    # If full_day is not 1, we need field 'hours'
    if kwargs.get('full_day', 0) == 0:
      required_fields.append('hours')

    for f in required_fields:
      if f not in kwargs.keys():
        raise KeyError('Missing required key \'{}\''.format(f))

    if not isinstance(kwargs['people_ids'], list):
      raise KeyError('Key \'{}\' not a list'.format('people_ids'))

    return self._post('timeoffs', kwargs)


  def create_timeoff_type(self, **kwargs):

    if 'timeoff_type_name' not in kwargs.keys():
      raise KeyError('Missing required key \'timeoff_type_name\'')

    return self._post('timeoff-types', kwargs)


  ## UPDATE ##
  
  def update_account(self, **kwargs):

    raise NotImplementedError('Not possible with API')


  def update_client(self, **kwargs):

    if 'client_id' not in kwargs.keys():
      raise KeyError('Missing required key \'client_id\'')

    return self._patch('clients/{}'.format(kwargs['client_id']), kwargs)


  def update_department(self, **kwargs):

    if 'department_id' not in kwargs.keys():
      raise KeyError('Missing required key \'department_id\'')

    return self._patch('departments/{}'.format(kwargs['department_id']), kwargs)


  def update_holiday(self, **kwargs):

    if 'holiday_id' not in kwargs.keys():
      raise KeyError('Missing required key \'holiday_id\'')

    return self._patch('holidays/{}'.format(kwargs['holiday_id']), kwargs)


  def update_milestone(self, **kwargs):

    if 'milestone_id' not in kwargs.keys():
      raise KeyError('Missing required key \'milestone_id\'')

    return self._patch('milestones/{}'.format(kwargs['milestone_id']), kwargs)


  def update_person(self, **kwargs):

    if 'people_id' not in kwargs.keys():
      raise KeyError('Missing required key \'people_id\'')

    return self._patch('people/{}'.format(kwargs['people_id']), kwargs)


  def update_project(self, **kwargs):

    if 'project_id' not in kwargs.keys():
      raise KeyError('Missing required key \'project_id\'')

    return self._patch('projects/{}'.format(kwargs['project_id']), kwargs)


  def update_task(self, **kwargs):

    if 'task_id' not in kwargs.keys():
      raise KeyError('Missing required key \'{}\''.format('task_id'))

    return self._patch('tasks/{}'.format(kwargs['task_id']), kwargs)


  def update_timeoff(self, **kwargs):

    if 'timeoff_id' not in kwargs.keys():
      raise KeyError('Missing required key \'{}\''.format('timeoff_id'))

    return self._patch('timeoffs/{}'.format(kwargs['timeoff_id']), kwargs)


  def update_timeoff_type(self, **kwargs):

    if 'timeoff_type_id' not in kwargs.keys():
      raise KeyError('Missing required key \'{}\''.format('timeoff_type'))

    return self._patch('timeoff-types/{}'.format(kwargs['timeoff_type_id']), kwargs)


  ## DELETE ##

  def delete_account(self, account_id):

    raise NotImplementedError('Not possible with Float API')


  def delete_client(self, client_id):

    return self._delete('clients/{}'.format(client_id))


  def delete_department(self, department_id):

    return self._delete('departments/{}'.format(department_id))


  def delete_holiday(self, holiday_id):

    return self._delete('holidays/{}'.format(holiday_id))


  def delete_milestone(self, milestone_id):

    return self._delete('milestones/{}'.format(milestone_id))


  def delete_person(self, person_id):

    return self._delete('people/{}'.format(person_id))


  def delete_project(self, project_id):

    return self._delete('projects/{}'.format(project_id))


  def delete_task(self, task_id):

    return self._delete('tasks/{}'.format(task_id))


  def delete_timeoff(self, timeoff_id):

    return self._delete('timeoffs/{}'.format(timeoff_id))


  def delete_timeoff_type(self, timeoff_type_id):

    raise NotImplementedError('Not possible with Float API')

    #return self._delete('timeoff-types/{}'.format(timeoff_type_id))
