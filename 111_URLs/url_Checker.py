import requests

def check_url(url):
    """
    Check if a given URL exists and returns its status code.
    Returns None if the URL does not exist or an exception is raised.
    """
    try:
        response = requests.get(url)
        return response.status_code
    except:
        return None

# Example usage
print(check_url("https://www.example.com")) # 200
print(check_url("https://www.example.com/nonexistent-page")) # 404
print(check_url("https://www.example-nonexistent.com")) # None
print(check_url("https://www.google.com")) # 200
