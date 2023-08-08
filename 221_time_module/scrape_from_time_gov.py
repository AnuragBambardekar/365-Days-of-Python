from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.time.gov/")
driver.maximize_window()

# Wait for the clock to load (you might need to adjust the time if necessary)
import time
time.sleep(5)  # Wait for 5 seconds

# Find the clock element and extract the time
clock_elem = driver.find_elements("xpath", "//div[@class='clock time-text']")
# time_text = clock_elem.find_element("time").text

# print("Current time:", clock_elem)

for elem in clock_elem:
    print(elem.get_attribute("innerHTML"))

# Close the browser
driver.quit()
