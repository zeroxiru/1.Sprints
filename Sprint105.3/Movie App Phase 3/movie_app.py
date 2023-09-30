from storage_json import StorageJson


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()

    def _command_movie_stats(self):
        pass

    def _generate_website(self):
        pass


    def menu(self):
        """
        Generates the menu text for the movie database application.

        Returns:
            str: The menu text.
        """
        return '''
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

    def command(self, command):
        """
        Executes the specified command based on user input.

        Args:
            command (int): The user's choice of command (0-9).
        """
        if command == 1:
            self._storage.list_movies()
        elif command == 2:
            # Get movie details from the user
            movie_title = input("Insert a name of the movie into the list:")
            movie_rating = float(input(" Provide a rating for the given movie:"))
            movie_year = int(input("Enter the year of the movie: "))
            self._storage.add_movie(movie_title, movie_year, movie_rating)
        elif command == 3:
            # Get movies name from the title given by user input
            movie = input("Type the movie name to delete from the database:")
            self._storage.delete_movie(movie)
        elif command == 4:
            # Get movie details from the user
            movie_title = input("Name of the movie into the list to update:")
            self._storage.show_single_movie_info(movie_title)
            movie_rating = float(input(" Provide a new rating for the given movie:"))
            self._storage.update_movie(movie_title, movie_rating)
        elif command == 5:
            self.show_stats()
        elif command == 6:
            self.random_movie()
        elif command == 7:
            movie_name = input("Enter the movie name to search from the movie database: ")
            self.search_movie(movie_name)
        elif command == 8:
            self.sorted_by_rating()
        elif command == 9:
            self.create_rating_histogram()
        elif command == 0:
            print("Bye!!!")

    def run(self):
        while True:
            command = int(input(self.menu()))
            if 0 <= command <= 9:
                self.command(command)  # Pass the 'command' value as an argument
            else:
                print("Choose between 0 to 9")
                continue
