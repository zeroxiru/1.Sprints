import requests
from datetime import datetime, timedelta

def fetch_top_song_on_birthday(birthday):
    # Convert the birthday to the required format for the Billboard API (YYYY-MM-DD)
    birthday_formatted = birthday.strftime("%Y-%m-%d")

    # Make a request to the Billboard API to fetch the top song on the birthday
    url = f"https://api.billboard.com/charts/hot-100/{birthday_formatted}"
    params = {
        "apikey": "YOUR_API_KEY",  # Replace with your actual API key
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Check if the request was successful and if there is a top song available
    if response.status_code == 200 and data["status"] == "ok" and data["songs"]:
        top_song = data["songs"][0]  # Get the first song from the chart
        song_name = top_song["title"]
        artist = top_song["artist"]

        # Fetch the lyrics using a Lyrics API (replace with the actual API and implementation)
        lyrics = fetch_lyrics(song_name, artist)  # Implement this function

        # Print the details
        print("Top Song on Your Birthday:")
        print("Song:", song_name)
        print("Artist:", artist)
        print("Lyrics:", lyrics)

    else:
        print("Unable to fetch the top song on your birthday.")

def fetch_lyrics(song_name, artist):
    # Replace "https://api.lyrics.ovh/v1/" with the actual Lyrics API endpoint
    url = f"https://api.lyrics.ovh/v1/{artist}/{song_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        lyrics = data["lyrics"]
        return lyrics
    else:
        print("Unable to fetch the lyrics.")
        return None

# Example usage:
birthday = datetime.strptime("28/06/1989", "%d/%m/%Y")
fetch_top_song_on_birthday(birthday)
