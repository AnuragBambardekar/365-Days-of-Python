from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

options = Options()
options.add_experimental_option("detach", True)

refresh_interval = int(input("Enter the refresh interval in seconds: "))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

url = "https://github.com/AnuragBambardekar"
driver.get(url)


try:
    while True:
        time.sleep(refresh_interval)
        driver.refresh()
except KeyboardInterrupt:
    print("Refreshing stopped by user.")
    driver.quit()
    sys.exit()
