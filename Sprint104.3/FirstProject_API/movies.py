from statistics import median
import random
import matplotlib.pyplot as plt
def list_movies():
    if movies != {}:
      i =1
      for key, val in movies.items():
        print(f'{i}. {key}: {val}')
        i +=1
    else:
        print('Movie is not available in the movie database collection')


def add_movies():
     movie = input("Insert a name of the movie into the list:")
     rating = float(input(" Provide a rating for the given movie:"))
     if not movie in movies:
       movies[movie] = rating
     else:
       movies[movie] += rating

def delete_movies():
      movie = input("Type the movie name to delete from the database:")
      if  movie in movies:
          print(f"{movie} = {movies[movie]}")
      else:
          print(f'{movie} was not found in the movie database')
      ask = input("Do you want to delete the movie Y/N")
      if "Y" in ask.upper():
          del movies[movie]
          print(f"{movie} is deleted from the movie db.")

def update_movies():
     movie = input("Type the movie name to update:")
     if movie in movies:
         print(f"{movie} = {movies[movie]}")
         ask = input("Do you want to update the movie Y/N")
         if "Y" in ask.upper():
          #new_movie_name = input("Update the name of the movie into the list:")
          new_rating = float(input("Enter the new rating for the movie: "))
          movies[movie] = new_rating
          #del movies[movie]
          print(f"{movie} has been added to the database with a rating of {new_rating} ")
         else:
             print(f"{movie} has not been updated.")
     else:
          print(f"{movie} was not not found in the movie database")

def show_stats():
    ratings = list(movies.values())
    if ratings:
        average = sum(ratings) / len(ratings)
        median_raiting = median(ratings)
        best_movie = max(movies, key=movies.get)
        worst_movie = min(movies, key=movies.get)

        print(f"Average rating: {average:.2f}")
        print(f"Median rating: {median_raiting:.2f}")
        print(f"Best movie: {best_movie} ({movies[best_movie]:.2f})")
        print(f"Worst movie: {worst_movie} ({movies[worst_movie]:.2f})")
    else:
        print("No movies available in the movie database.")

def random_movie():
    if movies:
        rand_movie =random.choice(list(movies.keys()))
        rand_rating = movies[rand_movie]
        print(f"Random Movie:{rand_movie} \t {rand_rating}")
    else:
        print("No movies available in the movie database.")

def search_movie():
    movie_name = input("Enter the movie name to search from the movie database: ")
    name_lower = movie_name.lower()

    found = False
    for movie_name, movie_rating in movies.items():
        if name_lower in movie_name.lower():
            print(f"The name of the movie for {movie_name} is: {movie_rating}")
            found = True
    if not found:
      print(f"No movie has found for the name: {movie_name}")

def sorted_by_rating():
    movies_sorted_by_rating = sorted(movies.items(), key=lambda item: item[1], reverse=True)

    if movies_sorted_by_rating:
        print("Movies sorted by rating: ")
        for movies_name, movies_rating in movies_sorted_by_rating:
           print(f"{movies_name}: {movies_rating}")
    else:
        print("No movies available in the movie database.")


def create_rating_histogram():
    ratings = list(movies.values())
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
   menu = '''
   ************ My Movies Databases ************
Menu:   
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Creating a rating histogram

Enter choice (1-10): \ '''
   while True:
      command = int(input(f"{menu} Choose between 1 to 10: "))
      if 0 < command < 11:
          if command ==1:
              list_movies()
          elif  command == 2:
              add_movies()
          elif command == 3:
              delete_movies()
          elif command == 4:
               update_movies()
          elif command == 5:
              show_stats()
          elif command == 6:
              random_movie()
          elif  command == 7:
              search_movie()
          elif command == 8:
              sorted_by_rating()
          elif command == 9:
              create_rating_histogram()
          elif command == 10:
              break
      else:
          print("Choose between 1 to 9")
          continue


if __name__ == "__main__":
   movies = {
       "The Shawshank Redemption": 9.5,
       "Pulp Fiction": 8.8,
       "The Room": 3.6,
       "The Godfather": 9.2,
       "The Godfather: Part II": 9.0,
       "The Dark Knight": 9.0,
       "12 Angry Men": 8.9,
       "Everything Everywhere All At Once": 8.9,
       "Forrest Gump": 8.8,
       "Star Wars: Episode V": 8.7
   }
main()
