import requests


def get_rates():
    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/latest"

    querystring = {"from": "USD", "to": "EUR,GBP"}

    headers = {
        "X-RapidAPI-Key": "666274c912msh4685d6a906c15c2p1b191ajsn680ad8cedf2e",
        "X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


def converter():
    url = "https://chatgpt53.p.rapidapi.com/"
    question = input("Enter your question for today: ")
    prompt = f"User question is {question}, the rates to convert you can get from here{get_rates()}, answer the " \
             f"question"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ],
        "temperature": 1
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "0c5d4fbc0amsh136a99e06add104p1d8436jsn34b5198a9f5c",
        "X-RapidAPI-Host": "chatgpt53.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    dictionary = response.json()
    answer = dictionary["choices"][0]["message"]["content"]
    print(answer)


def main():
    converter()


if __name__ == '__main__':
    main()