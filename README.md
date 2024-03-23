# Web Scraping Tool for Extracting URLs and Domain Names from Google Search Results
This Python script utilizes Selenium to automate web browsing and scraping of URLs and domain names from Google search results based on provided domain names. The tool also provides functionality to scroll down the search results dynamically to ensure all available URLs are captured.

# Prerequisites
Before running the script, ensure you have the following dependencies installed:

* Python 3.x
* Selenium
* Chrome WebDriver
* tkinter (should be pre-installed with Python)
 
You can install Python dependencies via pip:
pip install selenium

Download the Chrome WebDriver appropriate for your Chrome version from here and specify its path in the script.

# Usage
Run the script url_domain_extractor.py.

Select the CSV file containing the list of domain names when prompted.

The script will initiate a Google search for each domain and scrape URLs associated with each search result.
Extracted URLs will be saved in a CSV file named extracted_urls_<timestamp>.csv.
Extracted domain names will be saved in a CSV file named domain_names_<timestamp>.csv.

# Functionality
The script dynamically scrolls down the search results page to ensure all available URLs are captured.
It detects and handles scenarios where Google displays a message indicating more relevant results are available.
URLs are extracted using Selenium and parsed using the urllib library.
The script utilizes tkinter for file dialog to select the input CSV file.

# Important Notes
Ensure that you are not violating Google's terms of service or any website's terms of service while using this tool. Respect website policies and use web scraping responsibly.
The efficiency of the script may vary depending on network conditions and the number of URLs to be extracted.
Adjustments to sleep times and element selectors may be necessary based on changes to Google's HTML structure.
