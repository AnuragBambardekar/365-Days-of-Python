# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# from bs4 import BeautifulSoup

# options = Options()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                           options=options)

# driver.get("https://www.time.gov/")
# # driver.maximize_window()

# # Wait for the clock to load (you might need to adjust the time if necessary)
# import time
# time.sleep(5)  # Wait for 5 seconds

# # Find the clock element and extract the time
# clock_elem = driver.find_elements("xpath", "//div[@class='clock time-text']")
# clock_elem_title = driver.find_elements("xpath", "//div[@class='title']")
# clock_elem_subtitle = driver.find_elements("xpath", "//div[@class='sub-title']")


# # time_text = clock_elem.find_element("time").text

# # print("Current time:", clock_elem)

# for elem in clock_elem:
#     # print(elem.get_attribute("innerHTML"))

#     soup = BeautifulSoup(elem.get_attribute("innerHTML"), 'html.parser')
#     time_elements = soup.find_all('time')

#     for time_elem in time_elements:
#         # zoneoffset = time_elem['zoneoffset']
#         time_text = time_elem.get_text()
#         # print(f"Zoneoffset: {zoneoffset}, Time: {time_text}")
#         print(f"Time: {time_text}")

# print()

# for elem in clock_elem_title:
#     # print(elem.get_attribute("innerHTML"))
#     soup = BeautifulSoup(elem.get_attribute("innerHTML"), 'html.parser')
    
#     modified_html = str(soup).replace('<br>', ' ')
    
#     # Create a new BeautifulSoup object from the modified HTML
#     modified_soup = BeautifulSoup(modified_html, 'html.parser')
    
#     # Get the cleaned title text
#     title_text = modified_soup.get_text().strip()

#     print(title_text)

# print()

# for elem in clock_elem_subtitle:
#     # print(elem.get_attribute("innerHTML"))

#     soup = BeautifulSoup(elem.get_attribute("innerHTML"), 'html.parser')
    
#     modified_html = str(soup)
    
#     # Create a new BeautifulSoup object from the modified HTML
#     modified_soup = BeautifulSoup(modified_html, 'html.parser')
    
#     # Get the cleaned title text
#     sub_title_text = modified_soup.get_text().strip()
    
#     print(sub_title_text)

# # Close the browser
# driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.time.gov/")
# driver.maximize_window()

# Wait for the clock to load (you might need to adjust the time if necessary)
import time
time.sleep(5)  # Wait for 5 seconds

# Find the clock elements
clock_elem = driver.find_elements("xpath", "//div[@class='clock time-text']")
clock_elem_title = driver.find_elements("xpath", "//div[@class='title']")
clock_elem_subtitle = driver.find_elements("xpath", "//div[@class='sub-title']")

# Extract and print data in corresponding manner
for time_elem, title_elem, subtitle_elem in zip(clock_elem, clock_elem_title, clock_elem_subtitle):
    # Extract time
    soup_time = BeautifulSoup(time_elem.get_attribute("innerHTML"), 'html.parser')
    time_text = soup_time.find('time').get_text()

    # Extract title
    soup_title = BeautifulSoup(title_elem.get_attribute("innerHTML"), 'html.parser')
    title_text = soup_title.get_text().replace('<br>', ' ').strip()

    # Extract subtitle
    soup_subtitle = BeautifulSoup(subtitle_elem.get_attribute("innerHTML"), 'html.parser')
    subtitle_text = soup_subtitle.get_text().strip()

    print(f"Time: {time_text}, {title_text}, {subtitle_text}")

# Close the browser
driver.quit()
