import pyshorteners

url = input("Enter URL to shorten: ")

# initialize the shortener with the desired service (e.g. TinyURL, Bitly, etc.)
s = pyshorteners.Shortener()

# shorten the URL using the default service (TinyURL)
short_url = s.tinyurl.short(url)

print("Shortened URL:", short_url)
