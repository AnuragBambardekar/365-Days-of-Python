import requests

# number based on atmospheric noise
url = "https://www.random.org/integers/?num=1&min=0&max=100&col=5&base=10&format=plain&rnd=new"

number = requests.get(url)

print(number)
print(number.text)