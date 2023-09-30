import sys
from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

# def main():
#     """
#         The main entry point for the movie database application.
#
#         This function initializes the storage, creates a MovieApp object, and runs the application.
#
#         Returns:
#             None
#         """
#     print("######## Movie Database ########")
#     storage_option = int(input("Enter the number 1 to choose json and 2 for csv file format: "))
#     if storage_option == 1:
#         storage = StorageJson('movies_list.json')
#         print("You are now working on JSON file format")
#     elif storage_option == 2:
#         storage = StorageCsv('movies_list.csv')
#         print("You are now working on CSV file format")
#     else:
#         print("Invalid choice. Please enter 1 for JSON or 2 for CSV.")
#         return
#
#     movie_app = MovieApp(storage)
#     movie_app.run()
#


def main():
    if len(sys.argv) == 2:
        storage_file = sys.argv[1]
        # Determine storage type from the file extension
        storage_type = "JSON" if storage_file.lower().endswith(".json") else "CSV"
        print(f"Using {storage_type} storage")

        if storage_type == "JSON":
            storage = StorageJson(storage_file)
        elif storage_type == "CSV":
            storage = StorageCsv(storage_file)
        else:
            print("Invalid file extension. Please use JSON or CSV files.")
            return
    else:
        print("######## Movie Database ########")
        storage_option = int(input("Enter the number 1 to choose JSON and 2 for CSV file format: "))
        if storage_option == 1:
            storage = StorageJson('movies_list.json')
        elif storage_option == 2:
            storage = StorageCsv('movies_list.csv')
        else:
            print("Invalid choice. Please enter 1 for JSON or 2 for CSV.")
            return

    movie_app = MovieApp(storage)
    movie_app.run()

if __name__ == "__main__":
    main()


if __name__ == "__main__":

    main()
