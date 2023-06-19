"""
Read through this file to yourself OUT LOUD! Yes, out loud!
	- What does the APODConnection class do? What property does it have?
    - What does the AstonomyPhoto class do? What properties does it have?

Then, complete the show_photos() function on your own.

Bonus #1: Add a print statement between lines 25-26 to view all the photo data returned
by the API in your CLI. Choose some more data to show, then add it to the properties
in the AstronomyPhoto class and to the show_photos() function.

Bonus #2: Add a try/except block to handle unexpected errors.
"""


import requests

class APODConnection:

    def __init__(self):
        self.url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=6"

    def fetch_photo_data(self):
            """
            Return the URL for NASA's Astronomy Photo of the Day (APOD).
            """

            response = requests.get(self.url).json()
            return response


class AstronomyPhoto:

    def __init__(self):
        self.photo_url = None
        self.date = None
        self.title = None


def show_photos():
    """
    Write a function that uses the APODConnection class to call the NASA API,
    and use the AstronomyPhoto class to save and access the photo data.

    Make sure you only include the "image" media_type. We want to exclude videos for now.
    Print each photo_url to the console before the return statement.
    """
    pass