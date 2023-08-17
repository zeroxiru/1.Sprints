from statistics import median
import random
import matplotlib.pyplot as plt
import json
import requests

def fetch_movie_details(title):
    """
       Fetches movie details from the OMDb API using the movie title.

       Args:
           title (str): The title of the movie to search for.

       Returns:
           dict: A dictionary containing movie details (Title, Year, Rating, Poster).
                 Returns None if the movie is not found in the API or if there is an error.
       """
    api_key = '46a938ce'
    url = f'http://www.omdbapi.com/?apikey={api_key}&t={title}'
    try:
        response = requests.get(url)
        # Raise an exception for 4xx and 5xx status codes
        response.raise_for_status()
        data = response.json()
        if data["Response"] == True:
            movie_details = {
                "Title": data["Title"],
                "Year": int(data["Year"]),
                "Rating": float(data["imdbRating"]),
                "Poster": data["Poster"]
            }
            return movie_details
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie details: {e}")
    except (ValueError, KeyError) as e:
        print(f"Error parsing movie details from the API response: {e}")

    return None


def save_data(data, file_path):
    """
        Saves the data to a JSON file.

        Args:
            data (dict): The data to be saved (dictionary of dictionaries).
            file_path (str): The path to the JSON file.
        """
    with open(file_path, 'w') as file_obj:
        json.dump(data, file_obj, indent=4)


def list_movies(file_path):
    """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        The function loads the information from the JSON
        file and returns the data.

        For example, the function may return:
        {
          "Titanic": {
            "rating": 9,
            "year": 1999
          },
          "..." {
            ...
          },
        }
        """
    with open(file_path, "r") as file_obj:
        return json.load(file_obj)


def show_single_movie_info(file_path, title):
    movies_data = list_movies(file_path)
    if title in movies_data:
        movie_info = movies_data[title]
        print(f"{title}:")
        print(f"  Rating: {movie_info['rating']}")
        print(f"  Year: {movie_info['year']}")
    else:
        print(f"{title} was not found in the movie database.")


def add_movie(file_path, title):
    """
    Adds a movie to the movies database.

    Args:
        title (str): The title of the movie.
        year (int): The year of the movie.
        rating (float): The rating of the movie.
    """

    movies_data = list_movies(file_path)
    if title in movies_data:
        print(f"Movie {title} already exists in the database.")
        return

    movie_details = fetch_movie_details(title)
    if movie_details is not None:
        movies_data[title] = {
            "year": movie_details["Year"],
            "rating": movie_details["Rating"],
            "poster": movie_details["Poster"]
        }
        save_data(movies_data, file_path)
        print(f"Movie {title} successfully added.")
    else:
        print(f"Movie {title} not found in the OMDb API or error fetching details.")


def delete_movie(file_path, title_of_movie):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movie = title_of_movie
    movies_data = list_movies(file_path)
    if movie in movies_data:
        print(f"{movie} = {movies_data[movie]}")
        confirm = input(f"Do you want to delete {movie} from the movie database? (Y/N): ")
        if "Y" in confirm.upper():
            del movies_data[movie]
            save_data(movies_data, file_path)
            print(f"{movie} is deleted from the movie db.")
        else:
            print(f"{movie} was not deleted.")
    else:
        print(f'{movie} was not found in the movie database')


def update_movie(file_path, title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies_data = list_movies(file_path)

    if title in movies_data:
        movies_data[title]["rating"] = rating
        save_data(movies_data, file_path)
        print(f"{title} updated with rating {rating}.")
    else:
        print(f"{title} was not found in the movie database.")


def show_stats(file_path):
    '''
    It calculates the movies average, median, best and worst rating
    by using statistics library and print the movies from the movie database.

    If there are no movies in the database, it prints a message indicating that
    there are no movies available.
    '''
    movies_data = list_movies(file_path)
    ratings = [movie_info["rating"] for movie_info in movies_data.values()]
    if ratings:
        average = sum(ratings) / len(ratings)
        median_raiting = median(ratings)
        best_movie = max(movies_data, key=lambda title: movies_data[title]["rating"])
        worst_movie = min(movies_data, key=lambda title: movies_data[title]["rating"])

        print(f"Average rating: {average:.2f}")
        print(f"Median rating: {median_raiting:.2f}")
        print(f"Best movie: {best_movie} ({movies_data[best_movie]['rating']:.2f})")
        print(f"Worst movie: {worst_movie} ({movies_data[worst_movie]['rating']:.2f})")
    else:
        print("No movies available in the movie database.")


def random_movie(file_path):
    """
    It shows the random movies from the movie db.
    """
    movies_data = list_movies(file_path)
    if movies_data:
        rand_movie = random.choice(list(movies_data.keys()))
        rand_rating = movies_data[rand_movie]['rating']
        print(f'Randomd Movie: {rand_movie}\tRating:{rand_rating}')
    else:
        print("No movies available in the movie database.")


def search_movie(file_path, title_movie):
    """
        Search for movies in the movie database based on the given movie title.

        Args:
            file_path (str): The path to the JSON file containing the movies data.
            title_movie (str): The title of the movie to search for.

        Prints:
            The names, ratings, and years of the movies whose titles contain the given 'title_movie'.
            If no movie is found, it prints a message indicating that no movie was found.
        """


    def create_rating_histogram(file_path):
        """
        Creates a histogram of movie ratings based on the data in the movie database.

        Args:
            file_path (str): The path to the JSON file containing the movies data.

        Prints:
            Displays a histogram of movie ratings with the frequency of each rating.
            If there are no movies in the database, it prints a message indicating that no movies are available.
        """

    movies_data = list_movies(file_path)
    name_lower = title_movie.lower()
    found = False
    for title_movie, movie_info in movies_data.items():
        if name_lower in title_movie.lower():
            print(f"The name of the movie \"{title_movie}\" is: {movie_info['rating']} "
                  f"(Rating), {movie_info['year']} (Year)")

            found = True
    if not found:
        print(f"No movie has found for the name: {title_movie}")


def sorted_by_rating(file_path):
    """
           Sorts and displays movies in the movie database by their ratings in descending order.

           Args:
               file_path (str): The path to the JSON file containing the movies data.

           Prints:
               The names, ratings, and years of the movies, sorted by their ratings in descending order.
               If there are no movies in the database, it prints a message indicating that no movies are available.
           """
    movies_data = list_movies(file_path)
    movies_sorted_by_rating = sorted(movies_data.items(), key=lambda item: item[1]['rating'], reverse=True)
    if movies_sorted_by_rating:
        print("Movies sorted by rating:")
        for movie_name, movie_info in movies_sorted_by_rating:
            print(f"The name of the movie \"{movie_name}\" is: {movie_info['rating']}"
                  f"(Rating), {movie_info['year']} (Year)")
    else:
        print("No movies available in the movie database.")


def create_rating_histogram(file_path):
    """
            Creates a histogram of movie ratings based on the data in the movie database.

            Args:
                file_path (str): The path to the JSON file containing the movies data.

            Prints:
                Displays a histogram of movie ratings with the frequency of each rating.
                If there are no movies in the database, it prints a message indicating that no movies are available.
            """

    movies_data = list_movies(file_path)
    ratings = [movie_info['rating'] for movie_info in movies_data.values()]
    if ratings:
        plt.hist(ratings, bins=10, edgecolor='black')
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.title('Rating Histogram')
        file_name = input("Enter the file name to save the histogram (e.g., histogram.png): ")
        plt.savefig(file_name)
        plt.close()
        print(f"Histogram saved to {file_name}")
    else:
        print("No movies available in the movie database.")
