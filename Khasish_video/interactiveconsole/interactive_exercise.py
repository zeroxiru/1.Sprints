urls = [
    'https://edition.cnn.com/2023/03/09',
    'https://edition.cnn.com/2023/08/09',
    'https://edition.cnn.com/2022/03/09',
    'https://edition.cnn.com/2023/07/09',
    'https://edition.cnn.com/2019/01/09',
    'https://edition.cnn.com/2023/08/09',
    'https://edition.cnn.com/2023/05/09',
    'https://edition.cnn.com/2023/09/09'
]
for url in urls:
    tokens = url.split("/")
    if int(tokens[3]) % 2 == 0:
        print("Even")
    else:
        print("Odd")
   # print(url.split("/")[2])
#print(urls)