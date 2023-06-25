import requests

REQUEST_URL = "https://sallysbakingaddiction.com/?q="
OUTPUT_FILE = "output_file.html"

def saving_the_output_file(text, filename):
    try:
        with open(filename, "w") as fileobj:
            fileobj.write(text)
        print(f"File is saved in {filename}")
    except IOError as e:
        print(f"Error occurred while saving the file: {str(e)}")

def main():
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    #
    search_param = input("Please enter the dessert name: ")
    url = REQUEST_URL + search_param
    #response = requests.get(url, headers=headers)
    response = requests.get(url)
    if response.status_code == 200:
        saving_the_output_file(response.text, OUTPUT_FILE)
    else:
        print(f"Error occurred while fetching data. Status code: {response.status_code}")


if __name__ == '__main__':
    main()
