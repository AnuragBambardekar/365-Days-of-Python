import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is up!")
        else:
            print(f"Website returned a status code of {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Website is down or could not be reached.")

check_website("https://www.google.com")
