 Books to Scrape - Web Scraper

This is a Python script that scrapes book data from [Books to Scrape](https://books.toscrape.com/) and saves it to a CSV file.

## Features
- Extracts book titles, prices, star ratings, and stock availability.
- Scrapes data from 50 pages.
- Saves the data to `books.csv`.

## Requirements
Make sure you have the following installed:

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

You can install the dependencies using:

```bash
pip install -r requirements.txt
```
## Usage
Run the script:
```bash
python scrape_books.py
```
After running, you'll find the extracted data in books.csv

## Output Format
The CSV file will contain:

| Title         | Price | Star Rating | In Stock |
|--------------|-------|-------------|----------|
| Book Name 1  | 12.99 | Three       | True     |
| Book Name 2  | 8.49  | Five        | False    |





