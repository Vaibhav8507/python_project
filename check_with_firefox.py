# Initialize the Firefox WebDriver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
# Navigate to a website
driver.get("https://www.fusioncharts.com/features/export-charts-as-images-and-PDF")
time.sleep(5)
# link_text = "/features/export-charts-as-images-and-PDF#customize-titles-in-export-menu"  # Replace with the text of the link you want to click
link_text=driver.find_element(By.XPATH, "//a[@href='/features/export-charts-as-images-and-PDF#customize-titles-in-export-menu']")
link_text.click()
time.sleep(7)


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".raphael-group-186-button > rect:nth-child(3)"))).click()
time.sleep(10)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#chartobject-2 > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"))).click()
time.sleep(10)

download_directory = 'C:/Users/VNarule/Downloads'  # Replace with the directory where you saved the downloaded file
list_of_files = os.listdir(download_directory)
latest_file = max(list_of_files, key=lambda x: os.path.getctime(os.path.join(download_directory, x)))
file_path1 = os.path.join(download_directory, latest_file)
print(file_path1)
file_path = os.path.normpath(file_path1)
print(file_path)


  # Replace with your authentication token

# file_path = "D:\execute.png"


# URL where you want to upload the file
url = 'http://10.20.202.211/doc/api/v1/upload/1'

# Replace 'file_field' with the name of the file input field in your HTML form
# Specify the path to the file you want to upload
# file_path = 'path/to/your/file.pdf'

# Create a dictionary with the file to be uploaded
with open(file_path, 'rb') as file:
    files = {'file': (file_path, file)}
    headers = {'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJsZXZlbCI6IjAiLCJzdWIiOiJ7XCJpZFwiOlwiYWE0NDU3NTAtZDRjMC00YzEyLTgwNzYtNjEyYmE0MjI3MjJkXCIsXCJ1SWRcIjpcIjc2YTdiYmE2LTNjMDgtNDE4ZS05MmYxLTQ3NmRjMzY0MjJlZVwiLFwidUxldmVsXCI6XCIwXCIsXCJuYW1lXCI6XCJLaXJhbiBQYXRpbFwiLFwidG9rZW5JZFwiOm51bGx9IiwiaWF0IjoxNjk0NTAwNjgwLCJleHAiOjE2OTQ1NDM4ODB9.Q-_w37l-c5gKug0nzW6wxS5fYM1VkNXOm-vucRBM-eHGy_6YPRG9cHvq7ue1o4gojWR3lk7pnLliUKel7oDpiw'}

    # Make the POST request to upload the file
    payload = {}
    response = requests.post(url, headers=headers, data=payload, files=files)

    print(response.text)
    # response = requests.post(upload_url, files=files, headers=headers)

    # Check the response
    if response.status_code == 200:
        print("File uploaded successfully!")
    else:
        print("File upload failed with status code:", response.status_code)




# In the js_script section, you'll need to replace the comment with actual JavaScript code that identifies and clicks the specific FusionCharts element based on the chart's structure and your interaction requirements. This can be a complex task as it depends on the specific FusionCharts implementation and how elements are structured within it. You may need to inspect the FusionCharts in the browser's developer tools to determine the appropriate JavaScript logic for your case.










