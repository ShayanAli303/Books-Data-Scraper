import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

data = []
for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.find("p")["class"][1]

        data.append([title, price, availability, rating])
    time.sleep(1)
with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability", "Rating"])
    writer.writerows(data)