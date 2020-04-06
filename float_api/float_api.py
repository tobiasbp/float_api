import requests

#class ParameterMissingError(Exception):
#  pass

class UnexpectedStatusCode(Exception):
  """
  Raise this error when a call to the API
  returns a status code other than the one we expect
  """
  pass

class DataValidationError(Exception):
  """
  Raise this error if the API could not
  validate the data we gave it
  """

class FloatAPI():

  def __init__(self, access_token, application_name, contact_email):
    '''
    https://dev.float.com/overview_authentication.html
    '''

    # The session to use for all requests
    self.session = requests.Session()

    # Headers to send with every request
    self.headers = {
      "Authorization": "Bearer {}".format(access_token),
      "User-Agent": "{} ({})".format(application_name, contact_email)
      }

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

    # Raise exception on unexpected status code
    if r.status_code != 204:
      raise UnexpectedStatusCode("Got {} but expected 204".format(r.status_code))

    return True


  def _get(self, path, error_object, params = {}):
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

    # Raise exception on unexpected status code
    if r.status_code != 200:
      raise UnexpectedStatusCode("Got {} but expected 200".format(r.status_code))

    return r.json()


  def _get_all_pages(self, path, error_object, params = {}):
    """
    Args:
      path: The string added to the base URL
      error_object: The object to return if status code is not 200
      params: key,value pairs to send in URL
      pagination: per-page (Default 200), page
    """

    # If key 'per_page' is in params, change to key to 'per-page'.
    # Python does not allow '-' in variable names, but Float
    # parameter is called 'per-page'
    if 'per_page' in params.keys():
      params['per-page'] = params.pop('per_page') 

    # Set default objects per page
    if 'per-page' not in params:
      params['per-page'] = 200

    # Set default objects per page
    if 'page' not in params:
      params['page'] = 1

    # The list of data to return
    list_to_return = []

    # Build the URL
    url = self.base_url.format(path)

    # Perform request
    while True:
      # Request data
      r = self.session.get(url, headers=self.headers, params=params)

      # Throw AssertionError on unexpected status code
      if r.status_code != 200:
        raise UnexpectedStatusCode("Got {} but expected 200".format(r.status_code))

      # Get the list returned by the request
      l = r.json()

      # Add the new list to the list of data to return
      list_to_return += l

      # Exit loop if we are on the last page of results
      if int(r.headers['X-Pagination-Current-Page']) >= int(r.headers['X-Pagination-Page-Count']): 
        break

      # Next page
      params['page'] += 1


    # All records must be in the list to return
    assert int(r.headers['X-Pagination-Total-Count']) == len(list_to_return), "Get all returns all records"

    # Return the list of all records
    return list_to_return


  def _post(self, path, data):
    """
    Args:
      path: The string added to the base URL
      data: The data to post
    """

    # Build the URL
    url = self.base_url.format(path)

    # Post
    r = self.session.post(url, json=data, headers=self.headers)

    # Raise exception if data could not be validated
    if r.status_code == 422:
      raise DataValidationError("API could not validate the data you posted" )

    # Raise exception on unexpected status code
    if r.status_code != 201:
      raise UnexpectedStatusCode("Got {} but expected 201".format(r.status_code))

    return r.json()


  def _patch(self, path, data):
    """
    Args:
      path: The string added to the base URL
      data: The data to post
    """

    # Build the URL
    url = self.base_url.format(path)

    # Post
    r = self.session.patch(url, json=data, headers=self.headers)

    # Raise exception on unexpected status code
    if r.status_code != 200:
      raise UnexpectedStatusCode("Got {} but expected 200".format(r.status_code))

    return r.json()


  ## GET ##
  
  def get_account(self, account_id):

    raise NotImplementedError('Not possible with API')


  def get_client(self, client_id):
    '''Get a client'''
    return self._get('clients/{}'.format(client_id), {})


  def get_department(self, department_id):
    '''Get a department'''
    return self._get('departments/{}'.format(department_id), {})


  def get_holiday(self, holiday_id):
    '''Get a holiday'''
    return self._get('holidays/{}'.format(holiday_id), {})


  def get_milestone(self, milestone_id):
    '''Get a milestone'''
    return self._get('milestones/{}'.format(milestone_id), {})


  def get_project_milestones(self, project_id):
    '''Get a list of milestones for project_id'''
    return self._get('milestones', {}, {'project_id': project_id})


  def get_person(self, people_id):
    '''Get a person'''
    return self._get('people/{}'.format(people_id), {})


  def get_people_reports(self, start_date, end_date, people_id=None):
    '''Get people reports'''
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
    '''Get a project'''
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
    '''Get a task'''
    return self._get('tasks/{}'.format(task_id), {})


  def get_timeoff_type(self, timeoff_type_id):
    '''Get a timeoff type'''
    return self._get('timeoff-types/{}'.format(timeoff_type_id), {})


  ## GET ALL ##

  def get_all_accounts(self, fields=[]):
    '''Get all Float accounts'''
    params = {'fields': fields}
    return self._get_all_pages('accounts', [], params)


  def get_all_clients(self, fields=[]):
    '''Get all clients'''
    params = {'fields': fields}
    return self._get_all_pages('clients', [], params)


  def get_all_departments(self, fields=[]):
    '''Get all departments'''
    params = {'fields': fields}
    return self._get_all_pages('departments', [], params)


  def get_all_holidays(self, fields=[]):
    '''Get all holidays'''
    params = {'fields': fields}
    return self._get_all_pages('holidays', [], params)


  def get_all_milestones(self, fields=[]):
    '''Get all milestones'''
    params = {'fields': fields}
    return self._get_all_pages('milestones', [], params)


  def get_all_people(self, fields=[]):
    '''Get all people'''
    params = {'fields': fields}
    return self._get_all_pages('people', [], params)


  def get_all_projects(self, fields=[]):
    '''Get all clients'''
    params = {'fields': fields}
    return self._get_all_pages('projects', [], params)


  def get_all_tasks(self, fields=[]):
    '''Get all tasks'''
    params = {'fields': fields}
    return self._get_all_pages('tasks', [], params)


  def get_all_timeoffs(self, fields=[]):
    '''Get all timeoffs'''
    params = {'fields': fields}
    return self._get_all_pages('timeoffs', [], params)


  def get_all_timeoff_types(self, fields=[]):
    '''Get all timeoff types'''
    params = {'fields': fields}
    return self._get_all_pages('timeoff-types', [], params)


  ## CREATE ##

  def create_account(self, **kwargs):

    raise NotImplementedError('Not possible with API')


  def create_client(self, **kwargs):
    '''Create a client'''
    if 'name' not in kwargs.keys():
      raise KeyError('Missing required key \'name\'')

    return self._post('clients', kwargs)


  def create_department(self, **kwargs):
    '''Create a department'''
    if 'name' not in kwargs.keys():
      raise KeyError('Missing required key \'name\'')

    return self._post('departments', kwargs)


  def create_holiday(self, **kwargs):
    '''
    Invalid if a holiday on the same day exists
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


  def delete_person(self, people_id):

    return self._delete('people/{}'.format(people_id))


  def delete_project(self, project_id):

    return self._delete('projects/{}'.format(project_id))


  def delete_task(self, task_id):

    return self._delete('tasks/{}'.format(task_id))


  def delete_timeoff(self, timeoff_id):

    return self._delete('timeoffs/{}'.format(timeoff_id))


  def delete_timeoff_type(self, timeoff_type_id):

    raise NotImplementedError('Not possible with Float API')

    #return self._delete('timeoff-types/{}'.format(timeoff_type_id))
