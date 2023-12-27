import requests
from bs4 import BeautifulSoup
import re

def get_article_text(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text from the HTML
        article_text = ' '.join([p.get_text() for p in soup.find_all('p')])
        
        return article_text
    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

def calculate_reading_time(text, words_per_minute=200):
    # Count the number of words in the text
    words = re.findall(r'\b\w+\b', text)
    
    # Calculate the reading time in minutes
    reading_time_minutes = len(words) / words_per_minute
    
    return reading_time_minutes

if __name__ == "__main__":
    # Replace with the URL of the article you want to analyze
    article_url = "https://pythoncircle.com/post/763/the-rising-popularity-of-python/"
    
    # Get the text content of the article
    article_text = get_article_text(article_url)
    
    if article_text:
        # Calculate the reading time
        reading_time = calculate_reading_time(article_text)
        
        print(f"Estimated reading time: {reading_time:.2f} minutes")
