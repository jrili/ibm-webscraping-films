import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# Declare constants
TARGET_URL = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
TARGET_OUTPUT_CSV_FILE = "top_50_films.csv"
TARGET_DB_NAME = "Movies.db"
TARGET_DB_TABLE_NAME = "Top_50"
NUM_ENTRIES_TO_SCRAPE = 50

# Get the HTML code for the page
html_page = requests.get(TARGET_URL).text

# Parse the HTML code, get all the needed rows (with tag 'tr') from the first table
data = BeautifulSoup(html_page, "html.parser")
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

# Iterate through the rows to find the data from each column (with tag 'td')
count = 0
output_rows_list = []
for row in rows:
    if count < NUM_ENTRIES_TO_SCRAPE:
        cells = row.find_all('td')
        if len(cells) > 0:

            # For titles with hyperlinks, get the contents of the <a> tag
            # By default, extract film title directly through .contents
            film_title = cells[1].contents[0]
            film_title_hyperlink = cells[1].find('a')
            if film_title_hyperlink != None:
                film_title = film_title_hyperlink.contents[0]

            data_dict = {"Average Rank": int(cells[0].contents[0]),
                        "Film": str(film_title),
                        "Year": int(cells[2].contents[0])}
            print(f"Found row #{count}: {data_dict}")
            output_rows_list.append(data_dict)
            count = count + 1
    else:
        break
output_df = pd.DataFrame.from_dict(output_rows_list)

# Save output to CSV
print(output_df)
output_df.to_csv(TARGET_OUTPUT_CSV_FILE)
print(f"Saved CSV output to {TARGET_OUTPUT_CSV_FILE}")

# Save output to DB
with sqlite3.connect(TARGET_DB_NAME) as conn:
    output_df.to_sql(name=TARGET_DB_TABLE_NAME, con=conn, if_exists='replace', index=False)

print(f"Saved DB output to {TARGET_DB_NAME}")
