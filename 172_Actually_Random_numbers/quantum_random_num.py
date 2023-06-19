import requests

response = requests.get("https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint16")

print(response)

data = response.json()
random_int = data['data'][0]

print(random_int)