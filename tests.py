import requests

def test_jsonplaceholder_api_response():
    # Wysyłamy zapytanie GET do testowego api jsonplaceholder, upewniamy się, że zwrócony jest status 200, w innym przypadku generujemy błąd
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    assert response.status_code == 200, f"TEST 1: FAILED\n Error: Endpoint did not return status code 200 but {response.status_code} instead."

    # Parsujemy odpowiedź na jsona, upewniamy się, że jest w porządanym formacie, w innym przypadku generujemy błąd
    parsed_response_dict = response.json()
    assert isinstance(parsed_response_dict, dict), "TEST 1: FAILED\n Error: Parsed response data is not a dictionary."

    # Tworzymy liste pól, których oczekujemy w odpowiedzi i weryfikujemy czy faktycznie tam się znajdują, w innym przypadku generujemy błąd
    checked_fields = ["id", "title", "userId"]
    for field in checked_fields:
        assert field in parsed_response_dict, f"TEST 1: FAILED\n Error: {field} not found in response."
    
    # Wiadomość o pomyślnym zakończeniu testu
    print("TEST 1: PASSED")

def test_github_api_response():
    # Wysyłamy zapytanie GET do testowego api freetestapi zawierającego listę języków, upewniamy się, że zwrócony jest status 200, w innym przypadku generujemy błąd
    response = requests.get("https://freetestapi.com/api/v1/languages")
    assert response.status_code == 200, f"TEST 2: FAILED\n Error: Endpoint did not return status code 200 but {response.status_code} instead."

    # Parsujemy odpowiedź na jsona, upewniamy się, że jest w porządanym formacie, w innym przypadku generujemy błąd
    parsed_response_list = response.json()
    assert isinstance(parsed_response_list, list), "TEST 2: FAILED\n Error: Parsed response data is not a list."

    # Tworzymy liste pól, których oczekujemy w odpowiedzi i weryfikujemy czy faktycznie tam się znajdują, w innym przypadku generujemy błąd
    checked_languages = ["english", "polish", "spanish"]
    for item in checked_languages:
        found = False
        for language in parsed_response_list:
            # Jeżeli dany język znalazł się w odpowiedzi ustawiamy flagę found na True i wychodzimy z wewnętrznej pętli
            if item.title() in language.values():
                found = True
                break
        assert found, f"TEST 2: FAILED\n Error: {item} not found in response."
    
    # Wiadomość o pomyślnym zakończeniu testu
    print("TEST 2: PASSED")


def main():
    test_jsonplaceholder_api_response()
    test_github_api_response()

if __name__ == "__main__":
    main()