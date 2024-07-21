import sys
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime

if len(sys.argv) < 3:
    print("Enter both start and end ranges")
    sys.exit()

# Range of event numbers to loop through
start_range = sys.argv[1]
end_range = sys.argv[2]

# exit program if inputs invalid
if not start_range.isnumeric() or not end_range.isnumeric():
    print("Invalid inputs: ensure start and end ranges are numeric")
    sys.exit()

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
            # Fetch the HTML content
            response = requests.get(url)
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
