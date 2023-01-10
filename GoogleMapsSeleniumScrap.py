from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the Google Maps website
driver.get("https://www.google.com/maps")

# Locate the search box and enter a location
search_box = driver.find_element(By.XPATH, '//input[@id="searchboxinput"]')
search_box.send_keys("New York City, NY")

# Locate the search button and click it
search_button = driver.find_element(By.XPATH, '//button[@id="searchbox-searchbutton"]')
search_button.click()

# Wait for the page to load
driver.implicitly_wait(10)

# Locate the first result on the page and print its name
first_result = driver.find_element(By.XPATH, '//div[@class="section-result"]')
print(first_result.text)

# Close the browser
driver.quit()
