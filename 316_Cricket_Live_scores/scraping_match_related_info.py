from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json

from bs4 import BeautifulSoup

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.espncricinfo.com/live-cricket-score")
# driver.maximize_window()

import time
time.sleep(5)  # Wait for 5 seconds

# # Extract the text using Selenium
# element = driver.find_element('css selector', '.ci-team-score strong')
# text_410_4 = element.text

# # Print the extracted text
# print(text_410_4)

# element = driver.find_element('css selector', '.ci-team-score:nth-child(2) strong')
# text_128_4 = element.text

# # Print the extracted text
# print(text_128_4)

# # Extract the text using Selenium
# netherlands_text = element.text

# # Find the next match information
# next_match_element = driver.find_element(By.CSS_SELECTOR, 'a[href*="melbourne-renegades-women-vs-melbourne-stars-women"] .ds-text-tight-s')

# # Extract the text using Selenium
# stars_text = next_match_element.text

# # Print the extracted text
# print(netherlands_text)
# print(stars_text)

# Extract information from script tags
script_tags = driver.find_elements(By.TAG_NAME, 'script')
event_data = []

# Limit the number of scripts to extract
max_scripts = 6
scripts_extracted = 0

for script_tag in script_tags:
    script_text = script_tag.get_attribute('text')
    if script_text:
        try:
            json_data = json.loads(script_text)
            if '@type' in json_data and json_data['@type'] == 'Event':
                event_data.append(json_data)
                scripts_extracted += 1
                # Break after extracting the desired number of scripts
                if scripts_extracted == max_scripts:
                    break
        except json.JSONDecodeError:
            pass

# Print the extracted data
print("Event Data:")
for data in event_data:
    print("URL:", data.get("url", ""))
    print("Name:", data.get("name", ""))
    print("Description:", data.get("description", ""))
    print("Event Status:", data.get("eventStatus", ""))
    
    location = data.get("location", {})
    print("Location Name:", location.get("name", ""))
    
    start_date = data.get("startDate", "")
    end_date = data.get("endDate", "")
    print("Date:", start_date.split("T")[0] if start_date else "", "to", end_date.split("T")[0] if end_date else "")
    print()


# Extract information from specified HTML elements
# ds_text_elements = driver.find_elements(By.XPATH, "//span[@class='ds-text-compact-xs ds-mr-0.5']")
# ds_text_content = [element.text for element in ds_text_elements]

# print("\nDS Text Elements:")
# for text_content in ds_text_content:
#     print(text_content)

# Close the WebDriver
driver.quit()