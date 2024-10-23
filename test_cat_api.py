
import pytest
import requests
from requests.exceptions import RequestException
from unittest.mock import patch
from main2 import get_random_cat_image

def test_successful_request(requests_mock):
    # Mock the API response
    url = "https://api.thecatapi.com/v1/images/search"
    mock_response = [{"url": "https://cdn2.thecatapi.com/images/abc.jpg"}]
    requests_mock.get(url, json=mock_response, status_code=200)

    # вызов функции и проверка результата
    result = get_random_cat_image()
    assert result == "https://cdn2.thecatapi.com/images/abc.jpg"

def test_unsuccessful_request_status_code(requests_mock):
    # Mock a 404 response
    url = "https://api.thecatapi.com/v1/images/search"
    requests_mock.get(url, status_code=404)

    # вызов функции и проверка результата
    result = get_random_cat_image()
    assert result is None

def test_unsuccessful_request_exception():
    # Patch the requests.get method to raise an exception
    with patch('requests.get', side_effect=RequestException):
        result = get_random_cat_image()
        assert result is None

