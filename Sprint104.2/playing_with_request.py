import requests

Request_Url = "https://sallysbakingaddiction.com/#search/q=banana%20cake"
output_file_name = "output_file.html"

def saving_the_output_file(text, filename):
    with open("filename", "w") as fileobj:
        fileobj.write(text)

def main():
    search_param = input("please enter the desert name: ")
    url = Request_Url + search_param
    response = requests.get(url)
    saving_the_output_file(response.text, output_file_name)
    print(f"file is saved in {output_file_name}")


if __name__ == '__main__':
    main()


