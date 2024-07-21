# import sys
# sys.path.insert(0,'C:\\Users\\Jeded\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages')

import csv
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://lessons.hoofersailing.org/event/"


# Range of event numbers to loop through
start_event_number = 108300
end_event_number = 108450

# CSV file name
csv_file = "hoofer_lessons_data.csv"

# Open the CSV file for writing
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["Title", "Schedule", "URL"])
    
    # Loop through the event numbers
    for event_number in range(start_event_number, end_event_number + 1):
        # Construct the full URL
        url = f"{base_url}{event_number}"
        trimmed_url = f"lessons.hoofersailing.org/event/{event_number}"
        
        try:
            # Fetch the HTML content
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get the page title
            title = soup.find(class_="event-title").get_text(strip=True)
            time = soup.find(class_="event-schedule").get_text(strip=True)
                        
            # Write the data to the CSV file
            writer.writerow([title, time, trimmed_url])
            
            # Print the results to the console
            # print(f"Title: {title}")
            # print(f"Time: {time}")
            # print(f"URL: {url}")
            # print("-" * 50)
        
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")

# End of script
