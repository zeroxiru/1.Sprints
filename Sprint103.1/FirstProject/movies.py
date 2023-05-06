from statistics import median
def list_movies():
    if movies != {}:
      i =1
      for key, val in movies.items():
        print(f'{i}. {key}: {val}')
        i +=1
    else:
        print(f'{key} is not avialable in the movie database collection')


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

Enter choice (1-9): \ '''
   while True:
      command = int(input(f"{menu} Choose between 1 to 9: "))
      if 0 < command < 10:
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
              Random_movie()
          elif  command == 7:
              search_movie()
          elif command == 8:
              sorted_by_rating()
          elif command == 9:
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
