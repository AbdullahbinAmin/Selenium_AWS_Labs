from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open AWS website
driver.get("https://aws.amazon.com/")

# Take a screenshot
driver.save_screenshot("Screenshots/aws_website.png")

# Wait for 10 seconds to see the page
time.sleep(10)

# Close the browser
driver.quit()
