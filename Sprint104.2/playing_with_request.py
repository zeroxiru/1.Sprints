import requests

REQUEST_URL = "https://sallysbakingaddiction.com/?q="
OUTPUT_FILE = "output_file.html"

def saving_the_output_file(text, filename):
    with open(filename, "w") as fileobj:
        fileobj.write(text)

def main():
    search_param = input("please enter the desert name: ")
    url = REQUEST_URL + search_param
    response = requests.get(url)
    saving_the_output_file(response.text, OUTPUT_FILE)
    print(f"file is saved in {OUTPUT_FILE}")


if __name__ == '__main__':
    main()


