from istorage import IStorage
import json

class StorageJson(IStorage):
    def __init__(self, file_path):
        self._file_path = file_path
        self._movies_data = self.load_movies_data()

    def load_movies_data(self):
        """
                   Loads the JSON data from a file.

                   Args:
                       file_path (str): The path to the JSON file.

                   Returns:
                       dict: The loaded JSON data as a dictionary of dictionaries.
                   """
        with open(self._file_path, "r") as file_obj:
            return json.load(file_obj)

    def save_data(self):
        """
            Saves the data to a JSON file.
            """
        movie_info_to_save = {movie: info for movie, info in self._movies_data.items()}
        with open(self._file_path, "w") as file_obj:
            return json.dump(movie_info_to_save, file_obj, indent=4)


    def list_movies(self):
        if self._movies_data:
            print("List of Movies")
            for movie, info in self._movies_data.items():
                print(f'Movie Title: {movie}')
                print(f"Movie Rating: {info['rating']}")
                print(f"Movie Year{info['year']}")
        else:
            print("No available movies in the database.")


    def add_movie(self, title, year, rating, poster):
        if(title, year, rating, poster) not in self._movies_data:
            self._movies_data[title] = {
                'year': year,
                'rating': rating,
                'poster': poster
            }
            self.save_data()
            print(f"{title} movie has added into the database")
        else:
            print(
                f"A movie with title: {title}, rating: {rating}, and year: " \
                f"{year} already exists in the movies database.")




    def delete_movie(self, title):
        pass

    def update_movie(self, title, rating):
        pass




class StorageCsv(IStorage):
    def __init__(self):
        pass