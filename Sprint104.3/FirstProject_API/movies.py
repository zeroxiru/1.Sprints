import movies_storage_new

def main():
    global movies_data
    movies_data = movies_storage_new.load_movies_data("movies_list.json")
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
                movies_storage_new.list_movies()
            elif command == 2:
                # Get movie details from the user
                movie_title = input("Insert a name of the movie into the list:")
                movie_rating = float(input("Provide a rating for the given movie:"))
                movie_year = int(input("Enter the year of the movie: "))
                movies_storage_new.add_movie(movie_title, movie_year, movie_rating)
            elif command == 3:
                # Get movies name from the title given by user input
                movie = input("Type the movie name to delete from the database:")
                movies_storage_new.delete_movie(movie)
            elif command == 4:
                # Get movie details from the user
                movie_title = input("Name of the movie into the list to update:")
                movies_storage_new.show_single_movie_info(movie_title)
                movie_rating = float(input("Provide a new rating for the given movie:"))
                movies_storage_new.update_movie(movie_title, movie_rating)
            elif command == 5:
                movies_storage_new.show_stats()
            elif command == 6:
                movies_storage_new.random_movie()
            elif command == 7:
                movie_name = input("Enter the movie name to search from the movie database: ")
                movies_storage_new.search_movie(movie_name)
            elif command == 8:
                movies_storage_new.sorted_by_rating()
            elif command == 9:
                movies_storage_new.create_rating_histogram()
            elif command == 0:
                print("Bye!!!")
                break
        else:
            print("Choose between 1 to 9")
            continue

if __name__ == "__main__":
    main()
