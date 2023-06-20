from flask import Flask, render_template  # NEW
import jinja2  # NEW
import requests

app = Flask(__name__)  # NEW


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


@app.route('/')  # NEW
def show_photos():
    apod_connection = APODConnection()
    apod_photos = apod_connection.fetch_photo_data()

    photo_objects = []
    for photo in apod_photos:

        if photo["media_type"] == "image":
            photo_object = AstronomyPhoto()

            photo_object.photo_url = photo["url"]
            photo_object.date = photo["date"]
            photo_object.title = photo["title"]

            photo_objects.append(photo_object)

    return render_template('photos.html', photo_objects=photo_objects)  # NEW


# NEW
if __name__ == '__main__':
    # Run the Flask server locally
    app.run()