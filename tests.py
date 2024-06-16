import requests


def test_jsonplaceholder_api_response():
    request = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    assert request.status_code == 200, "Endpoint did not return status code 200 but {request.status_code} instead."

    parsed_request = request.json()
    assert isinstance(parsed_request, dict), "Parsed response data is not a dictionary"

    checked_fields = ["id", "title", "userId"]
    for field in checked_fields:
        assert field in parsed_request, f"{field} not found in response."


def main():
    test_jsonplaceholder_api_response()

