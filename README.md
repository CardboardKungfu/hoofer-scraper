# Hoofer Sailing Lessons Website Scraper

## Description
A handy tool for getting a preview of the next week of Hoofer Sailing Club lessons. All of the lessons are typically posted the night before, but they aren't published and visible on the event calendar. You'll have to do a little bit of sleuthing to find the most relevant event ID. Once you do, typically I check for the next 150 events. 

Hopefully this relieves some of frustrations around the bogged down lessons website. Cheers!

## Installation
1. Install python3, if not already installed
2. Create and Activate Python virtual environment
- `python3 -m venv hoofer-venv`
Windows
- `cd .\hoofer-venv\bin\activate`
macOS and Linux
- `source myenv/bin/activate`
3. Install Dependencies
- `pip install -r requirements.txt`

## Example Usage
`python3 hoofer-scraper.py 108300 108400`
This will loop through all the events in the range 108300 thru 108400. If a link isn't live, it'll skip it and print the below error to your terminal:
`Failed to fetch https://lessons.hoofersailing.org/event/108304: 404 Client Error: Not Found for url: https://lessons.hoofersailing.org/event/108304`

Doing this generates a `.csv` file, e.g. `07-21_1842-hoofer-lessons.csv`.

For easiest viewing, I typically open excel, go to the data tab, and import the data from a csv. It should load it into a table that you can sort to your hearts content.