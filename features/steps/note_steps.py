from behave import given, when, then
from utils.factory import NoteFactory
from utils.page_object import NoteApiPage

api = NoteApiPage()

@given('A valid note payload')
def step_impl(context):
    context.payload = NoteFactory.create_valid_payload()

@given('An invalid note payload missing title')
def step_impl(context):
    context.payload = NoteFactory.create_invalid_payload()

@given('The note repository is empty')
def step_impl(context):
    all_notes = api.get_all_notes().json()
    for note in all_notes:
        api.delete_note(note['id'])

@given('Existing notes in the system')
def step_impl(context):
    payload = NoteFactory.create_valid_payload()
    api.create_note(payload)

@given('An existing note ID')
def step_impl(context):
    payload = NoteFactory.create_valid_payload()
    response = api.create_note(payload)
    context.existing_note = response.json()
    context.note_id = context.existing_note['id']

@given('An invalid note ID "{invalid_id}"')
def step_impl(context, invalid_id):
    context.note_id = invalid_id

@given('A valid note payload for update')
def step_impl(context):
    context.update_payload = NoteFactory.create_valid_payload()


@when('I send a POST request to create a note')
def step_impl(context):
    context.response = api.create_note(context.payload)

@when('I send a GET request to fetch all notes')
def step_impl(context):
    context.response = api.get_all_notes()

@when('I send a GET request for this note ID')
def step_impl(context):
    context.response = api.get_note_by_id(context.note_id)

@when('I send a PUT request to update this note')
def step_impl(context):
    payload = getattr(context, 'update_payload', NoteFactory.create_valid_payload())
    context.response = api.update_note(context.note_id, payload)

@when('I send a DELETE request for this note ID')
def step_impl(context):
    context.response = api.delete_note(context.note_id)


@then('The response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

@then('The response should contain the correct note data')
def step_impl(context):
    data = context.response.json()
    assert data['title'] == context.payload['title']
    assert data['content'] == context.payload['content']

@then('The response list should be empty')
def step_impl(context):
    assert len(context.response.json()) == 0

@then('The response list should not be empty')
def step_impl(context):
    assert len(context.response.json()) > 0

@then('The response should match the requested note')
def step_impl(context):
    data = context.response.json()
    assert data['id'] == context.note_id

@then('The note should be updated successfully')
def step_impl(context):
    data = context.response.json()
    assert data['title'] == context.update_payload['title']
