import load_data
import argparse

def print_help():
    print("Available commands")
    print("help - Print the list of the available commands")
    print(" show_countries - prints the all countries of the ships, without duplicates")
    print(" top_countries <num_countries> - Prints a list of top countries with the most ships")


def print_countries(data):
    ships = data["data"]
    ship_countries = [ship["COUNTRY"] for ship in ships]
    unique_countries = sorted(set(ship_countries))
    print(" List of unique Countries")
    for country in unique_countries:
        print(country)

def print_top_countries(data, num_of_top_countries):
    # data: the list of ship data contains in the data dictionary
    # num_of_top_countries  which will return the top number of countries.

    # first_step - Initialize the empty dictionary
    country_counts = {}

    # second_step - Retrive the ships data from the data dictionary
    ships = data["data"]

    # third_step - iterate over each ship in the list of ships
    for ship in ships:
        # Generate the country data from ships
        country = ship["COUNTRY"]
        # if the country exist in the country_counts increase the counts by one
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1


    # sort the country_counts  dictionary by values in descending order,producng a list of tuples
    sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

    # print the top countries along with the number of count of the ships
    print(f'Top {num_of_top_countries} countries:')
    for count, country in sorted_countries[: num_of_top_countries]:
        print(f"{country}: {count} ships")



def mini_tasks_of_ship_details(data):
    ships = data["data"]
    total_ships = len(ships)
    print(f"Total number of ships are {total_ships}")

    ship_names = [ship["SHIPNAME"] for ship in ships]
    print("Ship  full names")
    for name in ship_names:
      print(name)

    ship_countries = [ship["COUNTRY"] for ship in ships]
    print("Number of Ship countries :")
    for country in ship_countries:
        print(country)

    unique_countries = list(set (ship_countries))
    print("List of unique ship countries")
    for country in unique_countries:
        print(country)

def main():

    parser = argparse.ArgumentParser(description="Ship data command line")
    parser.add_argument("command", help="command to execute", choices=["help", "show_countries", "top_countries", "mini_tasks"])
    parser.add_argument("args", nargs="*", help="additional argument for the command")
    args = parser.parse_args()

    all_data = load_data.load_data()
    if args.command == "help":
        print_help()
    elif args.command == "show_countries":
        print_countries(all_data)
    elif args.command == "top_countries":
        if len(args.args) != 1:
            print("Invalid aruments. Please provide the number of countries.")
        else:
            try:
                num_of_top_countries = int (args.args[0])
                print_top_countries(all_data, num_of_top_countries)
            except ValueError:
                print("Invalid argument. please provide valid number.")
    elif args.command == "mini_tasks":
        mini_tasks_of_ship_details(all_data)


if __name__ == "__main__":
    main()
