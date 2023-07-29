from statistics import median
import random
import matplotlib.pyplot as plt
import json


movies_data = None
def load_movies_data(file_path):
    """
       Loads the JSON data from a file.

       Args:
           file_path (str): The path to the JSON file.

       Returns:
           dict: The loaded JSON data as a dictionary of dictionaries.
       """
    with open(file_path, "r") as file_obj:
        return json.load(file_obj)

def save_data(data, file_path):
    """
    Saves the data to a JSON file.

    Args:
        data (dict): The data to be saved (dictionary of dictionaries).
        file_path (str): The path to the JSON file.
    """
    with open(file_path, 'w') as file_obj:
        json.dump(data, file_obj, indent=4)

def list_movies():
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

    if movies_data:
        print("List of Movies:")
        for movie_title, movie_info in movies_data.items():
            print(f"{movie_title}:")
            print(f"  Rating: {movie_info['rating']}")
            print(f"  Year: {movie_info['year']}")
    else:
        print("No movies available in the database.")

def show_single_movie_info(title):

    if title in movies_data:
        movie_info = movies_data[title]
        print(f"{title}:")
        print(f"  Rating: {movie_info['rating']}")
        print(f"  Year: {movie_info['year']}")
    else:
        print(f"{title} was not found in the movie database.")



def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movie_title = title
    movie_year = year
    movie_rating = rating

    if (movie_title, movie_rating, movie_year) not in movies_data.values():
        movies_data[movie_title] = {
        "year": movie_year,
        "rating": movie_rating
        }
        save_data(movies_data, "movies_list.json")
        print(f"{movie_title} added to the movies database.")
    else:
        print(
        f"A movie with title: {movie_title}, rating: {movie_rating}, and year: " \
        f"{movie_year} already exists in the movies database.")


def delete_movie(title_of_movie):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movie = title_of_movie
    if movie in movies_data:
        print(f"{movie} = {movies_data[movie]}")
        confirm = input(f"Do you want to delete {movie} from the movie database? (Y/N): ")
        if "Y" in confirm.upper():
            del movies_data[movie]
            save_data(movies_data, "movies_list.json")
            print(f"{movie} is deleted from the movie db.")
        else:
            print(f"{movie} was not deleted.")
    else:
        print(f'{movie} was not found in the movie database')




def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """

    if title in movies_data:
        movies_data[title]["rating"] = rating
        save_data(movies_data, 'movies_list.json')
        print(f"{title} updated with rating {rating}.")
    else:
        print(f"{title} was not found in the movie database.")


def show_stats():
    '''
    It calculates the movies average, median, best and worst rating
    by using statistics library and print the movies from the movie database.

    If there are no movies in the database, it prints a message indicating that
    there are no movies available.
    '''
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

def random_movie():
    """
    It shows the random movies from the movie db.
    """
    if movies_data:
        rand_movie = random.choice(list(movies_data.keys()))
        rand_rating = movies_data[rand_movie]['rating']
        print(f'Randomd Movie: {rand_movie}\tRating:{rand_rating}')
    else:
        print("No movies available in the movie database.")


def search_movie(title_movie):
    name_lower = title_movie.lower()
    found = False
    for title_movie, movie_info in movies_data.items():
        if name_lower in title_movie.lower():
            print(f"The name of the movie \"{title_movie}\" is: {movie_info['rating']} "
                  f"(Rating), {movie_info['year']} (Year)")

            found = True
    if not found:
      print(f"No movie has found for the name: {title_movie}")

def sorted_by_rating():
    movies_sorted_by_rating = sorted(movies_data.items(), key=lambda item: item[1]['rating'], reverse=True)
    if movies_sorted_by_rating:
        print("Movies sorted by rating:")
        for movie_name, movie_info in movies_sorted_by_rating:
            print(f"The name of the movie \"{movie_name}\" is: {movie_info['rating']}"
                  f"(Rating), {movie_info['year']} (Year)")
    else:
        print("No movies available in the movie database.")

def create_rating_histogram():
    movies_data = load_movies_data("movies_list.json")
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





def main():
    global movies_data
    movies_data = load_movies_data("movies_list.json")
    menu = '''
   ************ My Movies Databases ************
Menu: 
0. Exit  
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Creating a rating histogram


Enter choice (0-9):  '''
    while True:
      command = int(input(f"{menu} Choose between 0 to 9: "))
      if 0 <= command <= 9:
          if command ==1:
              list_movies()
          elif  command == 2:
              # Get movie details from the user
              movie_title = input("Insert a name of the movie into the list:")
              movie_rating = float(input(" Provide a rating for the given movie:"))
              movie_year = int(input("Enter the year of the movie: "))
              add_movie(movie_title, movie_year, movie_rating )

          elif command == 3:
              # Get movies name from the title given by user input
              movie = input("Type the movie name to delete from the database:")
              delete_movie(movie)
          elif command == 4:
              # Get movie details from the user
              movie_title = input("Name of the movie into the list to update:")
              show_single_movie_info(movie_title)
              movie_rating = float(input(" Provide a new rating for the given movie:"))
              update_movie(movie_title, movie_rating)
          elif command == 5:
              show_stats()
          elif command == 6:
              random_movie()
          elif  command == 7:
              movie_name = input("Enter the movie name to search from the movie database: ")
              search_movie(movie_name)
          elif command == 8:
              sorted_by_rating()
          elif command == 9:
              create_rating_histogram()
          elif command == 0:
              print("Bye!!!")
              break

      else:
          print("Choose between 1 to 9")
          continue


if __name__ == "__main__":
  main()
