import sqlite3

conn = sqlite3.connect("newness_scraping.db")  # Opens file if exists, else creates file

cursor = conn.cursor()

company_data = [
    ("Sephora", "https://www.sephora.com/", "https://www.sephora.com/brands-list"),
    ("Ulta", "https://www.ulta.com/", "https://www.ulta.com/brand/all"),
    ("Nordstrom", "https://www.nordstrom.com/", "https://www.nordstrom.com/brands-list/beauty?origin=topnav"),
]
cursor.executemany("INSERT INTO Company (name, url, brand_list_url) VALUES (?, ?, ?)", company_data)

conn.commit()

conn.close()