import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

# Scrape 50 pages of books
for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')

    articles = soup.find_all('article', class_='product_pod')

    for article in articles:
        image = article.find("img")
        title = image.attrs['alt']
        star = article.find('p')['class'][1]  # Extract star rating class
        price = float(article.find('p', class_="price_color").text[1:])  # Remove £ symbol
        stock_status = article.find('p', class_='instock availability').get_text(strip=True)
        in_stock = stock_status.lower() == "in stock"

        books.append([title, price, star, in_stock])

# Save to CSV
df = pd.DataFrame(books, columns=['Title', 'Price', 'Star Rating', 'In Stock'])
df.to_csv('books.csv', index=False)
