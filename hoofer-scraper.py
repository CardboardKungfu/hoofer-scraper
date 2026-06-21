# import sys
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Range of event numbers to loop through
start_range = 108850
end_range = 108900

start_range = int(start_range)
end_range = int(end_range)

csv_file = datetime.today().strftime('%m-%d_%H%M') + '-hoofer-lessons.csv'

# Open the CSV file for writing
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["Title", "Schedule", "Event URL", "Registration URL"])
    
    # Loop through the event numbers
    for event_number in range(start_range, end_range + 1):
        # Construct the full URL
        url = f"https://lessons.hoofersailing.org/event/{event_number}"
        trimmed_url = f"lessons.hoofersailing.org/event/{event_number}"
        register_url = f"lessons.hoofersailing.org/event/register/{event_number}"
        
        try:
            # Set user-agent
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
            }
            # Fetch the HTML content
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get the page title
            title = soup.find(class_="event-title").get_text(strip=True)
            time = soup.find(class_="event-schedule").get_text(strip=True)
                        
            # Write the data to the CSV file
            writer.writerow([title, time, trimmed_url, register_url])
        
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
