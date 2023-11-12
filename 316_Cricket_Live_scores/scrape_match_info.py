from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.espncricinfo.com/live-cricket-score")
# driver.maximize_window()

import time
time.sleep(5)  # Wait for 5 seconds

# ds_text_elements = driver.find_elements(By.XPATH, "//span[@class='ds-text-compact-xs ds-mr-0.5']")

# # Extract and print the desired content
# for i in range(min(12, len(ds_text_elements))):
#     ds_text_element = ds_text_elements[i]
    
#     # Extracting the text content from the span element
#     span_text = ds_text_element.text
    
#     # Find the adjacent strong element
#     strong_element = ds_text_element.find_element(By.XPATH, './following-sibling::strong')
    
#     # Extracting the text content from the strong element
#     strong_text = strong_element.text

#     # Print the combined content
#     combined_text = f"{span_text} {strong_text}"
#     print("Score Text:", combined_text)

# # Extract "Live" or "Result"
# live_result = driver.find_element(By.CLASS_NAME, "ds-text-tight-xs.ds-font-bold.ds-uppercase.ds-leading-5").text

# # Extract content of ds-text-tight-xs ds-truncate ds-text-typo-mid3
# description = driver.find_element(By.CLASS_NAME, "ds-text-tight-xs.ds-truncate.ds-text-typo-mid3").text

# # Extract href tag
# href_tag = driver.find_element(By.CLASS_NAME, "ds-text-tight-xs.ds-truncate.ds-text-typo-mid3 a").get_attribute("href")

# # Extract content of ICC Cricket World Cup
# icc_world_cup = driver.find_element(By.CLASS_NAME, "ds-text-tight-xs.ds-text-typo.ds-underline.ds-decoration-ui-stroke").text

# # Print the extracted data
# print("Live/Result:", live_result)
# print("Description:", description)
# print("Href tag:", href_tag)
# print("ICC Cricket World Cup:", icc_world_cup)


# result_elements = driver.find_elements(By.CLASS_NAME, "ds-text-tight-xs")

# # Iterate through the result elements and print their text
# for result_element in result_elements:
#     result_text = result_element.text.replace('\n', ' ')
#     print(result_text)

# Extract "Live" or "Result"
# live_result = driver.find_elements(By.CLASS_NAME, "ds-text-tight-xs.ds-font-bold.ds-uppercase.ds-leading-5").text


# # Extract href tag
# href_tag = driver.find_elements(By.CLASS_NAME, "ds-text-tight-xs.ds-truncate.ds-text-typo-mid3 a").get_attribute("href")

descriptions = driver.find_elements(By.CLASS_NAME, "ds-text-tight-xs.ds-truncate.ds-text-typo-mid3")
league_names = driver.find_elements(By.CLASS_NAME, "ds-text-tight-xs.ds-text-typo.ds-underline.ds-decoration-ui-stroke")
team_elements = driver.find_elements(By.XPATH, "//p[@class='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate']")
score_elements = driver.find_elements(By.XPATH, "//div[@class='ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap']//strong")
paragraph_elements = driver.find_elements(By.XPATH, "//p[@class='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo']")

# # Iterate through the elements and print the team and corresponding score
# for i in range(0, len(team_elements)):
#     team1 = team_elements[i].text
#     team2 = team_elements[i + 1].text
#     score1 = score_elements[i].text
#     score2 = score_elements[i + 1].text
#     # result = paragraph_elements[i // 2].text

#     print(f"Team: {team1} ({score1}) vs {team2} ({score2}), Result: {paragraph_elements[i].text}")
#     print("-" * 50)

min_length = min(len(team_elements), len(score_elements), len(paragraph_elements), len(league_names))

for i in range(min_length):
    # league_name = league_names[i].text
    description = descriptions[i].text
    team1 = team_elements[i * 2].text
    team2 = team_elements[i * 2 + 1].text
    score1 = score_elements[i].text
    score2 = score_elements[i * 2 + 1].text
    result = paragraph_elements[i].text

    print(f"Match: {team1} ({score1}) vs {team2} ({score2})")
    print(f"Description: {description}")
    print(f"Result/Status: {result}")
    # print(f"League: {league_name}")
    print("-" * 100)


# Close the WebDriver
driver.quit()


