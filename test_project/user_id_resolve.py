import requests


headers = {
    "accept: application/json"
}

r = requests.post("https://petstore.swagger.io/v2/pet", json={
    "id": "11",
  "category": {
    "id": "0",
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": "0",
      "name": "string"
    }
  ],
  "status": "available"
})
if r.status_code == 200:
    print("pass")
print(r.json())
