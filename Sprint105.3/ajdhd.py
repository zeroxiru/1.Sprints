import unittest
from unittest.mock import patch
import requests
import pytest

def get_astronomy_photo_coding_exercise_2(url):
    """
    Returns a response object from the APOD API even if
    the HTTP status code is >= 400
    """
    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        return e.response
    return response

class APITestCase(unittest.TestCase):

    @patch('requests.get')
    def test_valid_url(self, mock_get):
        # Mock the requests.get method
        mock_get.return_value.status_code = 200

        # Call the function with a valid URL
        result = get_astronomy_photo_coding_exercise_2("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

        # Assert that the function returns a response object
        self.assertIsInstance(result, requests.Response)

    @patch('requests.get')
    def test_wrong_or_missing_api_key(self, mock_get):
        # Mock the requests.get method
        mock_get.return_value.status_code = 401

        # Call the function with an invalid API key
        result = get_astronomy_photo_coding_exercise_2("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

        # Assert that the function returns the HTTP error response
        self.assertIsInstance(result, requests.Response)
        self.assertEqual(result.status_code, 401)

    @patch('requests.get')
    def test_404_error(self, mock_get):
        # Mock the requests.get method
        mock_get.return_value.status_code = 404

        # Call the function with a URL that returns a 404 error
        result = get_astronomy_photo_coding_exercise_2("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")

        # Assert that the function returns the HTTP error response
        self.assertIsInstance(result, requests.Response)
        self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    unittest.main()
