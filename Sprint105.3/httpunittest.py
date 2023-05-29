import pytest
import requests

"""
Write a unit test to make sure the input URL is valid
Write a unit test to handle the case where the API key is wrong or missing
Write a unit test to check for a 404 error

Remember: Google is your friend when you get stuck!
"""


def get_astronomy_photo_coding_exercise_2(url):
    """
    Returns a response object from the APOD API even if
    the HTTP status code is >= 400
    """
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    response = requests.get(url)

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        return e.response

    return response
