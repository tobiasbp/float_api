import os
import random
import string
import sys
from datetime import date
from datetime import timedelta

from pytest import fixture
from float_api import FloatAPI

# Get access token from environment variable
FLOAT_ACCESS_TOKEN = os.environ.get("FLOAT_ACCESS_TOKEN", None)

# Create a Float API instance
api = FloatAPI(
    FLOAT_ACCESS_TOKEN,
    "Unit testing of Python API wrapper float-api",
    "float-api-wrapper-unit-test@example.com",
)


def account_keys():
    return [
        "account_id",
        "name",
        "email",
        "account_type",
        "department_filter_id",
        "view_rights",
        "edit_rights",
        "active",
        "created",
        "modified",
    ]


def project_keys():
    return [
        "project_id",
        "name",
        "client_id",
        "color",
        "notes",
        "tags",
        "budget_type",
        "budget_total",
        "default_hourly_rate",
        "non_billable",
        "tentative",
        "active",
        "project_manager",
        "all_pms_schedule",
        "created",
        "modified",
    ]


def project_tag_keys():
    return ["tag_name" "project_id"]


def people_keys():
    return [
        "people_id",
        "name",
        "email",
        "job_title",
        "department",
        "notes",
        "avatar_file",
        "auto_email",
        "employee_type",
        "work_days_hours",
        "active",
        "people_type_id",
        "tags",
        "start_date",
        "end_date",
        "default_hourly_rate",
        "created",
        "modified",
    ]


def client_keys():
    return ["name", "client_id"]


def department_keys():
    return ["name", "department_id"]


def task_keys():
    return [
        "task_id",
        "project_id",
        "start_date",
        "end_date",
        "start_time",
        "hours",
        "people_id",
        "status",
        "priority",
        "name",
        "notes",
        "repeat_state",
        "repeat_end_date",
        "created_by",
        "created",
        "modified_by",
        "modified",
    ]


def loggedtime_keys():
    return [
        "logged_time_id",
        "date",
        "notes",
        "hours",
        "billable",
        "people_id",
        "project_id",
        "phase_id",
        "task_id",
        "task_name",
        "locked",
        "locked_date",
        "created",
        "created_by",
        "modified_by",
        "modified",
    ]


def milestone_keys():
    return ["milestone_id", "name", "project_id", "date", "end_date"]


def phase_keys():
    return [
        "phase_id",
        "project_id",
        "name",
        "start_date",
        "end_date",
        "color",
        "notes",
        "budget_total",
        "default_hourly_rate",
        "non_billable",
        "tentative",
        "active",
        "created",
        "modified",
    ]


def people_report_keys():
    return [
        "billable",
        "capacity",
        "department",
        "department_id",
        "futureBillable",
        "futureNonBillable",
        "futureOvertime",
        "futureScheduled",
        "name",
        "nonBillable",
        "overtime",
        "people_id",
        "people_type_id",
        "scheduled",
        "timeoff",
        "unscheduled",
    ]


def project_report_keys():
    return [
        "scheduled",
        "billable",
        "nonBillable",
        "name",
        "project_id",
        "client_id",
        "futureScheduled",
        "futureBillable",
        "futureNonBillable",
    ]


def holiday_keys():
    return ["holiday_id", "name", "date", "end_date"]


def timeoff_keys():
    return [
        "timeoff_id",
        "timeoff_type_id",
        "start_date",
        "end_date",
        "start_time",
        "hours",
        "timeoff_notes",
        "modified_by",
        "created_by",
        "created",
        "modified",
        "repeat_state",
        "repeat_end",
        "full_day",
        "people_ids",
    ]


def timeoff_type_keys():
    return ["timeoff_type_id", "timeoff_type_name", "color", "created_by"]


def random_string(length=32):
    """
    Return a random string of ASCII letters and
    digits of length 'length'
    """
    # The random string
    s = ""

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
    client = api.update_client(client_id=client["client_id"], name=name)
    assert isinstance(client, dict), "Updated client is a dict"
    assert set(client_keys()).issubset(client.keys()), "Updated client has all keys"
    assert client["name"] == name, "Name of client is updated"

    # Get a list of clients with a subset of fields
    f = set(["name", "client_id"])
    assert f.issubset(client_keys()), "Fields must be valid"
    clients = api.get_all_clients(fields=",".join(f))
    for c in clients:
        assert isinstance(c, dict), "Item in list is a dict"
        assert f == c.keys(), "Item in list has wanted fields"

    # Delete client
    r = api.delete_client(client["client_id"])
    assert r == True, "Deleted client"


# Create, update and delete a time_off_type
def test_timeoff_type():

    # Create a timeoff_type
    timeoff_type = api.create_timeoff_type(timeoff_type_name=random_string(32))
    assert isinstance(timeoff_type, dict), "New timeoff_type is a dict"
    assert set(timeoff_type_keys()).issubset(
        timeoff_type.keys()
    ), "New timeoff_type has all keys"

    # Update a timeoff_type
    timeoff_type_name = random_string(32)
    timeoff_type = api.update_timeoff_type(
        timeoff_type_id=timeoff_type["timeoff_type_id"],
        timeoff_type_name=timeoff_type_name,
    )
    assert isinstance(timeoff_type, dict), "Updated timeoff_type is a dict"
    assert set(timeoff_type_keys()).issubset(
        timeoff_type.keys()
    ), "Updated timeoff_type has all keys"
    assert (
        timeoff_type["timeoff_type_name"] == timeoff_type_name
    ), "Name of timeoff_type is updated"

    # Get a list of timeoff_types with a subset of fields
    f = set(["timeoff_type_name", "timeoff_type_id"])
    assert f.issubset(timeoff_type_keys()), "Fields must be valid"
    timeoff_types = api.get_all_timeoff_types(fields=",".join(f))
    for t in timeoff_types:
        assert isinstance(t, dict), "Item in list is a dict"
        assert f == t.keys(), "Item in list has wanted fields"

    # Get all timeoff_types
    timeoff_types = api.get_all_timeoff_types()
    assert isinstance(timeoff_types, list), "timeoff_types is a list"

    # Test keys in reports
    for t in timeoff_types:
        assert set(timeoff_type_keys()).issubset(t.keys()), "Timeoff type has all keys"

    # Delete timeoff_type
    # This is not supported by the API!?
    # r = api.delete_timeoff_type(timeoff_type['timeoff_type_id'])
    # assert r == True, "Deleted timeoff_type"


def test_timeoff():

    # Create a timeoff_type
    timeoff_type = api.create_timeoff_type(timeoff_type_name=random_string(32))
    assert isinstance(timeoff_type, dict), "New timeoff_type is a dict"
    assert set(timeoff_type_keys()).issubset(
        timeoff_type.keys()
    ), "New timeoff_type has all keys"

    # Create a person
    person = api.create_person(name=random_string(32))
    assert isinstance(person, dict), "New person is a dict"
    assert set(people_keys()).issubset(person.keys()), "New person has all keys"

    # Create timeoff
    day_in_future = date.today() + timedelta(weeks=2)
    timeoff_hours = api.create_timeoff(
        timeoff_type_id=timeoff_type["timeoff_type_id"],
        start_date=date.today().isoformat(),
        end_date=day_in_future.isoformat(),
        hours=4,
        people_ids=[person["people_id"]],
    )
    assert isinstance(timeoff_hours, dict), "New timeoff is a dict"
    assert set(timeoff_keys()).issubset(
        timeoff_hours.keys()
    ), "New timeoff has all keys"

    # Get a list of timeoffs with a subset of fields
    f = set(["hours", "timeoff_id"])
    assert f.issubset(timeoff_keys()), "Fields must be valid"
    timeoffs = api.get_all_timeoffs(fields=",".join(f))
    for t in timeoffs:
        assert isinstance(t, dict), "Item in list is a dict"
        assert f == t.keys(), "Item in list has wanted fields"

    # Delete length hours timeoff
    r = api.delete_timeoff(timeoff_hours["timeoff_id"])
    assert r == True, "Deleted timeoff"

    # Create an all day timeoff
    timeoff_all_day = api.create_timeoff(
        timeoff_type_id=timeoff_type["timeoff_type_id"],
        start_date=date.today().isoformat(),
        end_date=day_in_future.isoformat(),
        full_day=1,
        people_ids=[person["people_id"]],
    )
    assert isinstance(timeoff_all_day, dict), "New timeoff is a dict"
    assert set(timeoff_keys()).issubset(
        timeoff_all_day.keys()
    ), "New timeoff has all keys"

    # Update all day timeoff
    timeoff_notes = random_string(32)
    timeoff_all_day = api.update_timeoff(
        timeoff_id=timeoff_all_day["timeoff_id"], timeoff_notes=timeoff_notes
    )
    assert isinstance(timeoff_all_day, dict), "Updated timeoff is a dict"
    assert set(timeoff_keys()).issubset(
        timeoff_all_day.keys()
    ), "Updated timeoff has all keys"

    # Get all timeoffs
    timeoffs = api.get_all_timeoffs()
    assert isinstance(timeoffs, list), "All timeoffs is a list"
    for t in timeoffs:
        assert isinstance(t, dict), "Timeoff in list is a dict"
        assert set(timeoff_keys()).issubset(t.keys()), "Timeoff in list has all keys"

    # Delete all day timeoff
    r = api.delete_timeoff(timeoff_all_day["timeoff_id"])
    assert r == True, "Deleted timeoff"

    # Can not delete timeoff_type with API!

    # Delete person
    r = api.delete_person(person["people_id"])
    assert r == True, "Deleted person"


# Create, update and delete a holiday.
# Holidays must be in the future
# (Not past? Timezone diff between client & server is probably a factor)
# Can not create a holiday if one exists on the same date
def test_holiday():

    # Create a holiday (Must be in the future)
    day_in_future = date.today() + timedelta(days=14)
    holiday = api.create_holiday(name=random_string(32), date=day_in_future.isoformat())
    assert isinstance(holiday, dict), "New holiday is a dict"
    assert set(holiday_keys()).issubset(holiday.keys()), "New holiday has all keys"

    # Update a holiday
    name = random_string(32)
    holiday = api.update_holiday(holiday_id=holiday["holiday_id"], name=name)
    assert isinstance(holiday, dict), "Updated holiday is a dict"
    assert set(holiday_keys()).issubset(holiday.keys()), "Updated holiday has all keys"
    assert holiday["name"] == name, "Name of holiday is updated"

    # Get a list of holidays with a subset of fields
    f = set(["name", "holiday_id"])
    assert f.issubset(holiday_keys()), "Fields must be holiday keys"
    holidays = api.get_all_holidays(fields=",".join(f))
    for h in holidays:
        assert isinstance(h, dict), "Holiday in list is a dict"
        assert f == h.keys(), "Holiday in list has wanted fields"

    # Delete holiday
    r = api.delete_holiday(holiday["holiday_id"])
    assert r == True, "Deleted holiday"


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
        project_id=project["project_id"],
        start_date=date.today().isoformat(),
        end_date=date.today().isoformat(),
        hours=8,
        people_id=person["people_id"],
    )
    assert isinstance(task, dict), "New task is a dict"
    assert set(task_keys()).issubset(task.keys()), "New task has all keys"

    # Update notes of test task
    notes = random_string(32)
    task = api.update_task(task_id=task["task_id"], notes=notes)
    assert isinstance(task, dict), "Updated task is a dict"
    assert set(task_keys()).issubset(task.keys()), "Updated task has all keys"
    assert task["notes"] == notes, "Notes of task are updated"

    # Get a list of tasks with a subset of fields
    f = set(["name", "task_id"])
    assert f.issubset(task_keys()), "Fields must be task keys"
    tasks = api.get_all_tasks(fields=",".join(f))
    for t in tasks:
        assert isinstance(t, dict), "Task in list is a dict"
        assert f == t.keys(), "Task in list has wanted fields"

    # Delete test task
    r = api.delete_task(task["task_id"])
    assert r == True

    # Delete test person
    r = api.delete_person(person["people_id"])
    assert r == True

    # Delete test project
    r = api.delete_project(project["project_id"])
    assert r == True


# Create, update and delete a task
def test_loggedtime():

    # Create a test project
    project = api.create_project(name=random_string(32))
    assert isinstance(project, dict), "New project is a dict"
    assert set(project_keys()).issubset(project.keys()), "New project has all keys"

    # Create a test person
    person = api.create_person(name=random_string(32))
    assert isinstance(person, dict), "New person is a dict"
    assert set(people_keys()).issubset(person.keys()), "New person has all keys"

    # Create a Logged Time entry
    logged_time = api.create_logged_time(
        project_id=project["project_id"],
        date=date.today().isoformat(),
        hours=8,
        notes=random_string(32),
        people_id=person["people_id"],
    )
    assert isinstance(logged_time, dict), "New Logged Time is a dict"
    assert set(loggedtime_keys()()).issubset(
        logged_time.keys()
    ), "New Logged Time has all keys"

    # Update Logged Time entry
    notes = random_string(64)
    logged_time = api.update_logged_time(
        logged_time_id=logged_time["logged_time_id"], notes=notes
    )
    assert isinstance(logged_time, dict), "Updated task is a dict"
    assert set(loggedtime_keys()()).issubset(
        logged_time.keys()
    ), "Updated Logged Time has all keys"
    assert logged_time["notes"] == notes, "Notes of Logged Time are updated"

    # Get a list of tasks with a subset of fields
    f = set(["name", "logged_time_id"])
    assert f.issubset(loggedtime_keys()()), "Fields must be Logged Time keys"
    logged_times = api.get_all_logged_time(fields=",".join(f))
    for t in logged_times:
        assert isinstance(t, dict), "Logged Time in list is a dict"
        assert f == t.keys(), "Logged Time in list has wanted fields"

    # Delete test task
    r = api.delete_logged_time(logged_time["logged_time_id"])
    assert r == True

    # Delete test person
    r = api.delete_person(person["people_id"])
    assert r == True

    # Delete test project
    r = api.delete_project(project["project_id"])
    assert r == True


# Create, update and delete a person
def test_person():

    # Create a person
    person = api.create_person(name=random_string(32))
    assert isinstance(person, dict), "New person is a dict"
    assert set(people_keys()).issubset(person.keys()), "New person has all keys"

    # Update a person
    notes = random_string(32)
    person = api.update_person(people_id=person["people_id"], notes=notes)
    assert isinstance(person, dict), "Updated person is a dict"
    assert set(people_keys()).issubset(person.keys()), "Updated person has all keys"
    assert person["notes"] == notes, "Notes of person are updated"

    # Get a list of people with a subset of fields
    f = set(["name", "people_id"])
    assert f.issubset(people_keys()), "Fields must be person keys"
    people = api.get_all_people(fields=",".join(f))
    for p in people:
        assert isinstance(p, dict), "Person in list is a dict"
        assert f == p.keys(), "Person in list has wanted fields"

    # Delete person
    r = api.delete_person(person["people_id"])
    assert r == True, "Deleted person"


# Create, update and delete a project
def test_project():

    # Create a project
    project = api.create_project(name=random_string(32))
    assert isinstance(project, dict), "New project is a dict"
    assert set(project_keys()).issubset(project.keys()), "New project has all keys"

    # Update a project
    notes = random_string(32)
    project = api.update_project(project_id=project["project_id"], notes=notes)
    assert isinstance(project, dict), "Updated project is a dict"
    assert set(project_keys()).issubset(project.keys()), "Updated project has all keys"
    assert project["notes"] == notes, "Notes of project are updated"

    # Get a list of projects with a subset of fields
    f = set(["name", "project_id"])
    assert f.issubset(project_keys()), "Fields must be valid"
    projects = api.get_all_projects(fields=",".join(f))
    for p in projects:
        assert isinstance(p, dict), "Item in list is a dict"
        assert f == p.keys(), "Item in list has wanted fields"

    # Delete project
    r = api.delete_project(project["project_id"])
    assert r == True, "Deleted project"


# Create, update and delete a department
def test_department():

    # Create a department
    department = api.create_department(name=random_string(32))
    assert isinstance(department, dict), "New department is a dict"
    assert set(department_keys()).issubset(
        department.keys()
    ), "New department has all keys"

    # Update a department
    name = random_string(32)
    department = api.update_department(
        department_id=department["department_id"], name=name
    )
    assert isinstance(department, dict), "Updated department is a dict"
    assert set(department_keys()).issubset(
        department.keys()
    ), "Updated department has all keys"
    assert department["name"] == name, "Name of department is updated"

    # Get a list of departments with a subset of fields
    f = set(["name", "department_id"])
    assert f.issubset(department_keys()), "Fields must be valid"
    departments = api.get_all_departments(fields=",".join(f))
    for d in departments:
        assert isinstance(d, dict), "Item in list is a dict"
        assert f == d.keys(), "Item in list has wanted fields"

    # Delete department
    r = api.delete_department(department["department_id"])
    assert r == True, "Deleted department"


# Test people reports
def test_people_reports():

    # Get all people
    all_people = api.get_all_people()
    assert isinstance(all_people, list), "All people is a list"

    # Get reports
    future_date = date.today() + timedelta(weeks=4)
    people_reports = api.get_people_reports(
        start_date=date.today().isoformat(), end_date=future_date.isoformat()
    )
    assert isinstance(people_reports, list), "People report is a list"
    # assert len(people_reports) == len(all_people), "No of people reports match no of people"

    # Test keys in reports
    # FIXME: Fields in people report are not consistent
    # as of june 15th 2020. Must disable check.
    # for r in people_reports:
    #  assert set(people_report_keys()).issubset(r.keys()), "People report has all keys"


# Test project reports
def test_project_reports():

    # Get all projects
    all_projects = api.get_all_projects()
    assert isinstance(all_projects, list), "All projects is a list"

    # Get reports
    future_date = date.today() + timedelta(weeks=4)
    project_reports = api.get_project_reports(
        start_date=date.today().isoformat(), end_date=future_date.isoformat()
    )
    assert isinstance(project_reports, list), "Project report is a list"
    # assert len(project_reports) == len(all_projects), "No of project reports match no of project"

    # Test keys in reports
    for r in project_reports:
        assert set(project_report_keys()).issubset(
            r.keys()
        ), "Project report has all keys"


# Test get all functions
def test_get_all():

    functions = [
        (api.get_all_accounts, account_keys()),
        (api.get_all_clients, client_keys()),
        (api.get_all_departments, department_keys()),
        (api.get_all_people, people_keys()),
        (api.get_all_projects, project_keys()),
        (api.get_all_tasks, task_keys()),
        (api.get_all_logged_time(), loggedtime_keys()),
        (api.get_all_milestones, milestone_keys()),
        (api.get_all_phases, phase_keys()),
    ]

    for func, keys in functions:
        r = func()
        assert isinstance(keys, list), "Keys is a list"
        assert isinstance(r, list), "get all is a list"

        for c in r:
            assert isinstance(c, dict), "Get all list item is a dict"
            assert set(keys).issubset(c.keys()), "Dict has all keys" + str(func)


# Test milestones
def test_milestones():

    # Create a project
    project = api.create_project(name=random_string(32))
    assert isinstance(project, dict), "New project is a dict"
    assert set(project_keys()).issubset(project.keys()), "New project has all keys"

    # Create a milestone
    milestone = api.create_milestone(
        name=random_string(32),
        project_id=project["project_id"],
        date=date.today().isoformat(),
    )
    assert isinstance(milestone, dict), "New milestone is a dict"
    assert set(milestone_keys()).issubset(
        milestone.keys()
    ), "New milestone has all keys"

    # Update name of milestone
    name = random_string(32)
    milestone = api.update_milestone(milestone_id=milestone["milestone_id"], name=name)
    assert isinstance(milestone, dict), "Updated milestone is a dict"
    assert set(milestone_keys()).issubset(
        milestone.keys()
    ), "Updated milestone has all keys"
    assert milestone["name"] == name, "Name of milestone is updated"

    # Get a list of milestones with a subset of fields
    f = set(["name", "milestone_id"])
    assert f.issubset(milestone.keys()), "Fields must be valid"
    milestones = api.get_all_milestones(fields=",".join(f))
    for m in milestones:
        assert isinstance(m, dict), "Item in list is a dict"
        assert f == m.keys(), "Item in list has wanted fields"

    # Delete milestone
    r = api.delete_milestone(milestone["milestone_id"])
    assert r == True, "Deleted milestone"

    # Delete project
    r = api.delete_project(project["project_id"])
    assert r == True, "Deleted project"


# Test creation, get'ing and deletion
def test_create_get_delete():

    functions = [
        (
            api.create_client,
            api.delete_client,
            api.get_client,
            client_keys(),
            "client_id",
        ),
        (
            api.create_person,
            api.delete_person,
            api.get_person,
            people_keys(),
            "people_id",
        ),
        (
            api.create_project,
            api.delete_project,
            api.get_project,
            project_keys(),
            "project_id",
        ),
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
        # assert created_object == r, "Get newly created object: {}".format(f_get)

        # FIXME: Update

        # Delete object
        r = f_delete(r[o_id])

        assert r == True, "New object deleted" + str(f_delete)


# Create, update and delete a phase
def test_phase():

    # Create a test project
    project = api.create_project(name=random_string(32))
    assert isinstance(project, dict), "New project is a dict"
    assert set(project_keys()).issubset(project.keys()), "New project has all keys"

    # Create a test phase
    phase = api.create_phase(
        project_id=project["project_id"],
        name=random_string(32),
        start_date=date.today().isoformat(),
        end_date=date.today().isoformat(),
    )
    assert isinstance(phase, dict), "New phase is a dict"
    assert set(phase_keys()).issubset(phase.keys()), "New phase has all keys"

    # Get a phase
    phase = api.get_phase(phase_id=phase["phase_id"])
    assert isinstance(phase, dict), "Phase is a dict"
    assert set(phase_keys()).issubset(phase.keys()), "Phase has all keys"

    # Update a phase
    name = random_string(32)
    phase = api.update_phase(phase_id=phase["phase_id"], name=name)
    assert isinstance(phase, dict), "Updated phase is a dict"
    assert set(phase_keys()).issubset(phase.keys()), "Updated phase has all keys"
    assert phase["name"] == name, "Name of phase is updated"

    # Delete test phase
    r = api.delete_phase(phase["phase_id"])
    assert r == True

    # Delete test project
    r = api.delete_project(project["project_id"])
    assert r == True
