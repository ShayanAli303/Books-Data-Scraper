# Books Data Scraper

This project is a Python-based web scraper that extracts book data from a multi-page website and stores it in a structured CSV file.

## Features

- Scrapes data from multiple pages (pagination handling)
- Extracts structured information:
  - Book Title
  - Price
  - Availability
  - Rating
- Saves clean data into a CSV file
- Simple and efficient scraping logic

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV

## How It Works

The script sends HTTP requests to each page of the website, parses the HTML content using BeautifulSoup, and extracts relevant data fields. The collected data is then stored in a CSV file.

## How to Run

1. Install required libraries:
   ```bash
   pip install requests beautifulsoup4
