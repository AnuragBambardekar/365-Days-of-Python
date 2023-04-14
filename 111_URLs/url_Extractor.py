import requests
from bs4 import BeautifulSoup

def extract_urls_to_file(url, output_file):
    """
    Extract all URLs from a given webpage and write them to a file.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        with open(output_file, 'w') as f:
            for link in soup.find_all('a'):
                f.write(link.get('href') + '\n')
    except:
        pass

# Example usage
extract_urls_to_file("https://www.google.com", "urls.txt")

