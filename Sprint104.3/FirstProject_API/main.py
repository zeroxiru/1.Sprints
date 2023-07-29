import json
import movies_storage

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
