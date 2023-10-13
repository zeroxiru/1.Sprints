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
        if storage_option not in (1, 2):
            print("Invalid choice. Please enter 1 for JSON or 2 for CSV.")
            return

        # determine Storage type depending on the choice.

        if storage_option == 1:
            storage_type = "JSON"
        elif storage_option == 2:
            storage_type = "CSV"
        else:
            print("Invalid choice. Please enter 1 for JSON or 2 for CSV.")
            return

    # Ask for the family member's name (e.g., sara, john, jack)
    family_member_name = input("Enter the family member's name (sara,john, jack): ")

    # Construct the storage file name based on the family member's name
    Storage_file_name = f"{family_member_name.lower()}.json"

    # Initialize the storage based on the selected format and the family member's name
    if storage_type == "JSON":
        storage = StorageJson(Storage_file_name, family_member_name)
    else:
        storage = StorageCsv(Storage_file_name, family_member_name)
    print(f"You are now working on {storage_type} file format for {family_member_name}'s storage.")



    # Create the MovieApp instance with the family storage
    movie_app = MovieApp(storage)
     # Create separate storage instances for John, Sara, and Jack
    family_storage = {
        'John': StorageJson('john.json', 'John'),
        'Sara': StorageJson('sara.json', 'Sara'),
        'Jack': StorageJson('jack.json', 'Jack'),
    }
    movie_app._family_storage = family_storage

    for family_member_name, storage_instance in family_storage.items():
        storage_instance._command_movie_stats(movie_app)

    movie_app.run()

if __name__ == "__main__":
    main()

