import requests
import json

urls = ["https://reqres.in/api/users", "http://www.absolutelynothing.com", "http://www.absolutelynothing.com/something", "http://doesthisevenexist.com"]

def save_res_to_file(name, res):
    file_name =f'file_{name}'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(res)


def main():
    for i, url in enumerate(urls):
        print(f"Sending get request to url: {url}")

        try:
            res = requests.get(url)
        except requests.exceptions.ConnectionError as error:
            print('Connection Error: ', error)
        else:
            try:
                json_res = json.dumps(res.json())
                save_res_to_file(i,json_res)
            except requests.exceptions.JSONDecodeError:
                save_res_to_file(i, res.text)


if __name__ == '__main__':
    main()

# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()
#     for user in data["data"]:
#
#         print(user["url"])
# else:
#     print("status code", response.status_code)