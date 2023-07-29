from statistics import median
import random
import matplotlib.pyplot as plt
import json


class MovieDb:

    def __init__(self, file_path):
        self.file_path = file_path
        self.movies_data = self.load_movies_data()

    def load_movies_data(self):
        """
           Loads the JSON data from a file.

           Args:
               file_path (str): The path to the JSON file.

           Returns:
               dict: The loaded JSON data as a dictionary of dictionaries.
           """
        with open(self.file_path, "r") as file_obj:
            return json.load(file_obj)

    # def save_data(self):
    #     """
    #     Saves the data to a JSON file.
    #
    #     Args:
    #         data (dict): The data to be saved (dictionary of dictionaries).
    #         file_path (str): The path to the JSON file.
    #     """
    #     with open(self.file_path, 'w') as file_obj:
    #         json.dump(self, file_obj, indent=4)
    def save_data(self):
        """
        Saves the data to a JSON file.
        """
        data_to_save = {movie: info for movie, info in self.movies_data.items()}
        with open(self.file_path, 'w') as file_obj:
            json.dump(data_to_save, file_obj, indent=4)

    def list_movies(self):
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

        if self.movies_data:
            print("List of Movies:")
            for movie_title, movie_info in self.movies_data.items():
                print(f"{movie_title}:")
                print(f"  Rating: {movie_info['rating']}")
                print(f"  Year: {movie_info['year']}")
        else:
            print("No movies available in the database.")

    def show_single_movie_info(self, title):

        if title in self.movies_data:
            movie_info = self.movies_data[title]
            print(f"{title}:")
            print(f"  Rating: {movie_info['rating']}")
            print(f"  Year: {movie_info['year']}")
        else:
            print(f"{title} was not found in the movie database.")

    def add_movie(self, title, year, rating):
        """
        Adds a movie to the movies database.
        Loads the information from the JSON file, add the movie,
        and saves it. The function doesn't need to validate the input.
        """

        if (title, rating, year) not in self.movies_data.values():
            self.movies_data[title] = {
                "year": year,
                "rating": rating
            }
            self.save_data()
            print(f"{title} added to the movies database.")
        else:
            print(
                f"A movie with title: {title}, rating: {rating}, and year: " \
                f"{year} already exists in the movies database.")

    def delete_movie(self, title_of_movie):
        """
        Deletes a movie from the movies database.
        Loads the information from the JSON file, deletes the movie,
        and saves it. The function doesn't need to validate the input.
        """
        movie = title_of_movie
        if movie in self.movies_data:
            print(f"{movie} = {self.movies_data[movie]}")
            confirm = input(f"Do you want to delete {movie} from the movie database? (Y/N): ")
            if "Y" in confirm.upper():
                del self.movies_data[movie]
                self.save_data()
                print(f"{movie} is deleted from the movie db.")
            else:
                print(f"{movie} was not deleted.")
        else:
            print(f'{movie} was not found in the movie database')

    def update_movie(self, title, rating):
        """
        Updates a movie from the movies database.
        Loads the information from the JSON file, updates the movie,
        and saves it. The function doesn't need to validate the input.
        """

        if title in self.movies_data:
            self.movies_data[title]["rating"] = rating
            self.save_data()
            print(f"{title} updated with rating {rating}.")
        else:
            print(f"{title} was not found in the movie database.")

    def show_stats(self):
        '''
        It calculates the movies average, median, best and worst rating
        by using statistics library and print the movies from the movie database.

        If there are no movies in the database, it prints a message indicating that
        there are no movies available.
        '''
        ratings = [movie_info["rating"] for movie_info in self.movies_data.values()]
        if ratings:
            average = sum(ratings) / len(ratings)
            median_raiting = median(ratings)
            best_movie = max(self.movies_data, key=lambda title: self.movies_data[title]["rating"])
            worst_movie = min(self.movies_data, key=lambda title: self.movies_data[title]["rating"])

            print(f"Average rating: {average:.2f}")
            print(f"Median rating: {median_raiting:.2f}")
            print(f"Best movie: {best_movie} ({self.movies_data[best_movie]['rating']:.2f})")
            print(f"Worst movie: {worst_movie} ({self.movies_data[worst_movie]['rating']:.2f})")
        else:
            print("No movies available in the movie database.")

    def random_movie(self):
        """
        It shows the random movies from the movie db.
        """
        if self.movies_data:
            rand_movie = random.choice(list(self.movies_data.keys()))
            rand_rating = self.movies_data[rand_movie]['rating']
            print(f'Randomd Movie: {rand_movie}\tRating:{rand_rating}')
        else:
            print("No movies available in the movie database.")

    def search_movie(self, title_movie):
        name_lower = title_movie.lower()
        found = False
        for title_movie, movie_info in self.movies_data.items():
            if name_lower in title_movie.lower():
                print(f"The name of the movie \"{title_movie}\" is: {movie_info['rating']} "
                      f"(Rating), {movie_info['year']} (Year)")

                found = True
        if not found:
            print(f"No movie has found for the name: {title_movie}")

    def sorted_by_rating(self):
        movies_sorted_by_rating = sorted(self.movies_data.items(), key=lambda item: item[1]['rating'], reverse=True)
        if movies_sorted_by_rating:
            print("Movies sorted by rating:")
            for movie_name, movie_info in movies_sorted_by_rating:
                print(f"The name of the movie \"{movie_name}\" is: {movie_info['rating']}"
                      f"(Rating), {movie_info['year']} (Year)")
        else:
            print("No movies available in the movie database.")

    def create_rating_histogram(self):

        ratings = [movie_info['rating'] for movie_info in self.movies_data.values()]
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

    def main(self):
        # movies_db = MovieDb(self, "movies_list.json")
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
                if command == 1:
                    self.list_movies()
                elif command == 2:
                    # Get movie details from the user
                    movie_title = input("Insert a name of the movie into the list:")
                    movie_rating = float(input(" Provide a rating for the given movie:"))
                    movie_year = int(input("Enter the year of the movie: "))
                    self.add_movie(movie_title, movie_year, movie_rating)

                elif command == 3:
                    # Get movies name from the title given by user input
                    movie = input("Type the movie name to delete from the database:")
                    self.delete_movie(movie)
                elif command == 4:
                    # Get movie details from the user
                    movie_title = input("Name of the movie into the list to update:")
                    self.show_single_movie_info(movie_title)
                    movie_rating = float(input(" Provide a new rating for the given movie:"))
                    self.update_movie(movie_title, movie_rating)
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
                    break

            else:
                print("Choose between 1 to 9")
                continue

def main():
    m = MovieDb("movies_list.json")
    m.main()


if __name__ == "__main__":
    main()
