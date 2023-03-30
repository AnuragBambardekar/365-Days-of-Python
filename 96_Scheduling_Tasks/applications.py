import requests
import os
import schedule
import time

def download_image():
    # Define the URL of the website that hosts the images
    url = 'https://source.unsplash.com/random'

    # Send a GET request to the website and download the image data
    response = requests.get(url)
    img_data = response.content

    # Save the image to disk
    filename = f'img_{time.strftime("%Y%m%d-%H%M%S")}.jpg'
    with open(filename, 'wb') as f:
        f.write(img_data)

    print(f'Downloaded image: {filename}')

# Schedule the image downloading task to run every 10 seconds
schedule.every(10).seconds.do(download_image)

while True:
    schedule.run_pending()
    time.sleep(1)
