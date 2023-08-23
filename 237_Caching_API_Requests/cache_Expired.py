import json
import requests
import os
import time

def is_cache_expired(json_cache, expiration_time):
    if not os.path.exists(json_cache):
        return True  # Cache doesn't exist, so it's expired
    current_time = time.time()
    cache_time = os.path.getmtime(json_cache)
    return (current_time - cache_time) > expiration_time

def fetch_data(*, update: bool = False, json_cache: str, url: str, cache_expiration: int = 1800):
    if update or is_cache_expired(json_cache, cache_expiration):
        json_data = None
    else:
        try:
            with open(json_cache, 'r') as file:
                json_data = json.load(file)
                print('Fetched data from local cache!')
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"No local cache found... {e}")
            json_data = None

    if not json_data:
        print('Fetching new json data... (Creating local cache)')
        json_data = requests.get(url).json()
        with open(json_cache, 'w') as file:
            json.dump(json_data, file)
        # Update the cache timestamp
        os.utime(json_cache, (time.time(), time.time()))

    return json_data

if __name__ == '__main__':
    url = "https://dummyjson.com/comments"
    json_cache = '237_Caching_API_Requests/comments_expiry.json'
    
    # Set the cache expiration time to 30 minutes (1800 seconds)
    cache_expiration = 1800

    data: dict = fetch_data(update=False, json_cache=json_cache, url=url, cache_expiration=cache_expiration)

    print(data)
