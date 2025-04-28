import requests
from behave import given, when, then
from hamcrest import assert_that, equal_to, has_entry, has_item


@given('I have the API endpoint "{endpoint}"')
def step_given_api_endpoint(context, endpoint):
    context.endpoint = endpoint


@when(u'I send a POST request with')
def step_impl(context):
    # Get data from the feature table
    data = {
        "name": context.table[0]["name"],
        "age": int(context.table[0]["age"]),
        "profession": context.table[0]["profession"]
    }

    response = requests.post(context.endpoint, json=data)
    context.response = response
    context.posted_data = data
    context.created_id = response.json().get('id')  # Save the generated ID

    print(f"POST Request Debug:\n"
          f"Sent Data: {data}\n"
          f"Status Code: {response.status_code}\n"
          f"Response: {response.json()}\n"
          f"Generated ID: {context.created_id}")


@then('the response status code should be {status_code:d}')
def step_then_check_status_code(context, status_code):
    assert_that(context.response.status_code, equal_to(status_code))


@then('the response should contain the created person data')
def step_then_check_response_contains_data(context):
    response_data = context.response.json()
    assert_that(response_data, has_entry("name", context.posted_data["name"]))
    assert_that(str(response_data["age"]), equal_to(str(context.posted_data["age"])))
    assert_that(response_data, has_entry("profession", context.posted_data["profession"]))


@when('I send a GET request to "{endpoint}"')
def step_when_send_get_request(context, endpoint):
    response = requests.get(endpoint)
    context.response_get = response
    context.get_data = response.json()
    print("GET Response:", context.get_data)


@then('the GET response should contain the created record')
def step_then_verify_record_in_get_response(context):
    assert_that(context.response_get.status_code, equal_to(200))

    # Buscar el registro creado en el array de respuesta
    found_records = [
        record for record in context.get_data
        if record.get('id') == context.created_id
    ]

    assert len(found_records) > 0, f"No se encontró el registro con ID {context.created_id} en la respuesta GET"

    record = found_records[0]
    assert_that(record, has_entry("name", context.posted_data["name"]))
    assert_that(str(record["age"]), equal_to(str(context.posted_data["age"])))
    assert_that(record, has_entry("profession", context.posted_data["profession"]))

    print(f"Registro encontrado en GET response: {record}")