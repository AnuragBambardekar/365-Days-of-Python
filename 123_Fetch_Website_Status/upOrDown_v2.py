import requests

"""
Allow the user to input a list of website URLs to check, rather than checking one website at a time.
Implement a timeout for the HTTP request, so that the program doesn't hang indefinitely if the website is not responding.
"""

def check_websites(urls, timeout=5):
    results = []
    for url in urls:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                results.append((url, True))
            else:
                results.append((url, False))
        except requests.exceptions.RequestException as e:
            results.append((url, False))
    return results

# Example usage:
urls = ["https://www.google.com", "https://www.yahoo.com", "https://www.example.com"]
results = check_websites(urls, timeout=3)
for url, is_up in results:
    status = "up" if is_up else "down"
    print(f"{url} is {status}")
