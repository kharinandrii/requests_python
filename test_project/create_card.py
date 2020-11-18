import requests


def create_card():
    headers = {
        "Accept": "application/json",
    }

    r = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=available', headers=headers)
    print(r.json())


    r2 = requests.get('https://petstore.swagger.io/v2/pet/11', headers=headers)
    print(r2.json())

create_card()
