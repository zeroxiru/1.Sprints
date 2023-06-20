import requests


class APODConnection:
    """
    A class for connecting to NASA's Astronomy Picture of the Day (APOD) API.
    """

    def __init__(self):
        """
        Initialize the APODConnection object with the API URL.
        """
        self.url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=6"

    def fetch_photo_data(self):
        """
        Fetch the photo data from the APOD API.

        Returns:
            list: List of photo data in JSON format.
        """
        response = requests.get(self.url).json()
        return response


class AstronomyPhoto:
    """
    A class representing a single astronomy photo with relevant attributes.
    """

    def __init__(self):
        """
        Initialize the AstronomyPhoto object with empty attributes.
        """
        self._photo_url = None
        self._date = None
        self._title = None
        self._explanation = None
        self._hd_url = None

    @property
    def photo_url(self):
        """
        Get the URL of the photo.

        Returns:
            str: The URL of the photo.
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, value):
        """
        Set the URL of the photo.

        Args:
            value (str): The URL of the photo.
        """
        self._photo_url = value

    @property
    def date(self):
        """
        Get the date of the photo.

        Returns:
            str: The date of the photo.
        """
        return self._date

    @date.setter
    def date(self, value):
        """
        Set the date of the photo.

        Args:
            value (str): The date of the photo.
        """
        self._date = value

    @property
    def title(self):
        """
        Get the title of the photo.

        Returns:
            str: The title of the photo.
        """
        return self._title

    @title.setter
    def title(self, value):
        """
        Set the title of the photo.

        Args:
            value (str): The title of the photo.
        """
        self._title = value

    @property
    def explanation(self):
        """
        Get the explanation of the photo.

        Returns:
            str: The explanation of the photo.
        """
        return self._explanation

    @explanation.setter
    def explanation(self, value):
        """
        Set the explanation of the photo.

        Args:
            value (str): The explanation of the photo.
        """
        self._explanation = value

    @property
    def hd_url(self):
        """
        Get the HD URL of the photo.

        Returns:
            str: The HD URL of the photo.
        """
        return self._hd_url

    @hd_url.setter
    def hd_url(self, value):
        """
        Set the HD URL of the photo.

        Args:
            value (str): The HD URL of the photo.
        """
        self._hd_url = value

    @classmethod
    def show_photos(cls):
        """
        Fetch and display the astronomy photos from the APOD API.

        Make sure to include only the photos with the "image" media_type.

        Print each photo URL, title, date, explanation, and HD URL to the console.
        """
        connection = APODConnection()
        try:
            response = connection.fetch_photo_data()
            for item in response:
                if item["media_type"] == "image":
                    photo = cls()
                    photo.photo_url = item.get("url")
                    photo.date = item.get("date")
                    photo.title = item.get("title")
                    photo.explanation = item.get("explanation")
                    photo.hd_url = item.get("hdurl")

                    # Print the photo data
                    print("Title:", photo.title)
                    print("Date:", photo.date)
                    print("URL:", photo.photo_url)
                    print("Explanation:", photo.explanation)
                    print("HD URL:", photo.hd_url)
                    print("--------------------------------")

                else:
                    print("Invalid media type:", item.get("media_type"))

        except requests.RequestException as e:
            print("Error occurred while fetching photo data:", str(e))


if __name__ == '__main__':
    AstronomyPhoto.show_photos()
