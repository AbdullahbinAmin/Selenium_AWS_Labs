import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

# Initialize the WebDriver (automatically manages ChromeDriver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the AWS website
    driver.get("https://aws.amazon.com/")

    # Capture a screenshot
    screenshot_path = "screenshot.png"
    driver.save_screenshot(screenshot_path)

    # Upload the screenshot to the S3 bucket
    bucket_name = os.getenv('S3_BUCKET_NAME')
    object_name = 'screenshot.png'
    s3.upload_file(screenshot_path, bucket_name, object_name)
    print(f"Screenshot uploaded to S3 bucket: {bucket_name}/{object_name}")

finally:
    # Wait for visibility and close the browser
    time.sleep(10)
    driver.quit()

    # Clean up local screenshot file
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)