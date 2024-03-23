import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from urllib.parse import urlparse

# Function to create a file dialog and get the input CSV file path
def browse_for_csv():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path
def scroll_down(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Adjust the sleep time as needed
        
        # Check if scrolling reached the bottom
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if "In order to show you the most relevant results" in driver.page_source:
                    print("Encountered relevant results message. Breaking scroll.")
                    break
        
        if new_height == last_height:
            # Check if "More results" button exists
            more_button_exists = False
            try:
                more_button = driver.find_element(by=By.CLASS_NAME, value="GNJvt.ipz2Oe")  # Adjust class name
                more_button_exists = True
                more_button.click()
                time.sleep(2)  # Adjust the sleep time after clicking more results button
            except:
                pass
            if(last_height == new_height and not more_button_exists):
                break
                
        
        last_height = new_height
        

def extract_domain(url):
     domain = urlparse(url).netloc
     return domain

chrome_driver_path = "C:/Users/sudha/Downloads/chromedriver-win64/chromedriver.exe"
os.environ["CHROME_DRIVER_PATH"] = chrome_driver_path

driver = webdriver.Chrome()

# Browse for the input CSV file containing domain names
domain_file = browse_for_csv()
if not domain_file:
    print("No file selected. Exiting.")
    exit()

# Read domain names from the selected CSV file
with open(domain_file, 'r') as csvfile:
    domain_reader = csv.reader(csvfile)
    domain_names = [row[0] for row in domain_reader]

# Set to store all extracted URLs
all_extracted_urls = set()

# Loop through domain names
for domain in domain_names:
    search_url = f"https://www.google.com/search?q=site:{domain}"
    driver.get(search_url)
    
    scroll_down(driver)

    page_source = driver.page_source
    

    start_marker = "UWckNb"
    end_marker = "data-ved"

    start_index = page_source.find(start_marker)
    end_index = page_source.find(end_marker, start_index)

    extracted_urls = set()

    while start_index != -1 and end_index != -1:
        text_to_split = page_source[start_index:end_index]

        role_text_start = "href=\""
        split_text = text_to_split.split(role_text_start)

        for item in split_text[1:]:
            extracted_text = item.split("\"")[0].strip()
            if extracted_text.startswith("http"):
                extracted_urls.add(extracted_text)

        start_index = page_source.find(start_marker, end_index)
        end_index = page_source.find(end_marker, start_index)

    all_extracted_urls.update(extracted_urls)

# Close the WebDriver

# Generate timestamp for filename
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Define CSV filename for extracted URLs
csv_urls_filename = f"extracted_urls_{timestamp}.csv"

# Write all extracted URLs to a single CSV file
with open(csv_urls_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for url in all_extracted_urls:
        csv_writer.writerow([url])

print(f"CSV file '{csv_urls_filename}' has been created with all the extracted URLs.")
# Extract domain names from the URLs
domains = set()
for url in all_extracted_urls:
    domain = extract_domain(url)
    domains.add(domain)
# Define CSV filename for domain names
csv_domains_filename = f"domain_names_{timestamp}.csv"
# Write all extracted domain names to a single CSV file
with open(csv_domains_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for domain in domains:
        csv_writer.writerow([domain])
print(f"CSV file '{csv_domains_filename}' has been created with all the extracted domain names.")