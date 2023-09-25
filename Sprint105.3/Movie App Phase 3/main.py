

# def main():
#     """
#         The main function to interact with the movie database.
#
#         This function displays a menu to the user and allows them to perform various operations on the movie database.
#         The user can choose from options like listing movies, adding a new movie, deleting a movie,
#         updating a movie's rating, viewing statistics, getting a random movie, searching for a movie by title,
#         sorting movies by rating, and creating a rating histogram.
#
#         The function reads the movie data from a JSON file and performs the chosen operation on it.
#         After each operation, the updated data is saved back to the JSON file.
#
#         Usage:
#         1. The function expects a JSON file containing the movie data to exist beforehand. If it doesn't exist, the
#            function will raise an error.
#         2. The user will be presented with a menu and prompted to choose an option from 0 to 9.
#         3. Based on the user's choice, the corresponding function from the movie_storage module will be called to
#            perform the desired operation on the movie data.
#         4. The updated movie data will be saved back to the JSON file after each operation.
#
#         Note:
#         - The movie_storage module contains functions to handle operations related to the movie database, such as
#           loading data, saving data, adding, deleting, and updating movies.
#         - The menu options and their descriptions will be displayed to the user at the beginning of each iteration.
#
#         Returns:
#         None
#         """
#
#     file_path = "movies_list.json"
#     menu = '''
#    ************ My Movies Databases ************
# Menu:
# 0. Exit
# 1. List movies
# 2. Add movie
# 3. Delete movie
# 4. Update movie
# 5. Stats
# 6. Random movie
# 7. Search movie
# 8. Movies sorted by rating
# 9. Creating a rating histogram
#
# Enter choice (0-9):  '''
#     while True:
#         command = int(input(f"{menu} Choose between 0 to 9: "))
#         if 0 <= command <= 9:
#             if command == 1:
#                 movies_data = movies_storage.list_movies(file_path)
#                 if movies_data:
#                     print("List of Movies:")
#                     for movie_title, movie_info in movies_data.items():
#                         print(f"{movie_title}:")
#                         print(f"  Rating: {movie_info['rating']}")
#                         print(f"  Year: {movie_info['year']}")
#                 else:
#                     print("No movies available in the database.")
#             elif command == 2:
#                 # Get movie details from the user
#                 title = input("Enter new movie name: ")
#                 year = int(input("Enter the year of the movie: "))
#                 rating = float(input("Provide a rating for the given movie: "))
#                 movies_storage.add_movie(file_path, title, year, rating)
#             elif command == 3:
#                 # Get movies name from the title given by user input
#                 movie = input("Type the movie name to delete from the database:")
#                 movies_storage.delete_movie(file_path, movie)
#             elif command == 4:
#                 # Get movie details from the user
#                 movie_title = input("Name of the movie into the list to update:")
#                 movies_storage.show_single_movie_info(file_path, movie_title)
#                 movie_rating = float(input("Provide a new rating for the given movie:"))
#                 movies_storage.update_movie(file_path, movie_title, movie_rating)
#             elif command == 5:
#                 movies_storage.show_stats(file_path)
#             elif command == 6:
#                 movies_storage.random_movie(file_path)
#             elif command == 7:
#                 movie_name = input("Enter the movie name to search from the movie database: ")
#                 movies_storage.search_movie(file_path, movie_name)
#             elif command == 8:
#                 movies_storage.sorted_by_rating(file_path)
#             elif command == 9:
#                 movies_storage.create_rating_histogram(file_path)
#             elif command == 0:
#                 print("Bye!!!")
#                 break
#         else:
#             print("Choose between 1 to 9")
#             continue

if __name__ == "__main__":
    pass
    #main()
