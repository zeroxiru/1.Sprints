from movie_app import MovieApp
from storage_json import StorageJson

class Main():
    def __init__(self):
        # Initialize your class and any data structures here
        pass

    def main(self):
        """
        Main entry point for the movie database application.
        Displays a menu and handles user commands.
        """
        while True:
            command = int(input(self.menu()))
            if 0 <= command <= 9:
                self.command(command)
            else:
                print("Choose between 0 to 9")
                continue

def main():
    storage = StorageJson('movies.json')
    movie_app = MovieApp(storage)
    movie_app.run()

if __name__ == "__main__":
    main
