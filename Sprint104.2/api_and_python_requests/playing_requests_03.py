import requests

REQUEST_URL = "https://sallysbakingaddiction.com/#search/q="

OUTPUT_FILE = "output_file.html"

def save_output_file(text, file_name):
    with open(file_name, "w") as fileobj:
        fileobj.write(text)


def main():
    search_param = input("Enter the name of the dessert:")
    url = REQUEST_URL + search_param
    res = requests.get(url)
    save_output_file(res.text, OUTPUT_FILE)
    print(f"file is saved in {OUTPUT_FILE}")


if __name__ == '__main__':
    main()

