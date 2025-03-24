import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
target_output_csv_file = "top_50_films.csv"
target_db_name = "Movies.db"
target_db_table_name = "Top_50"

columns = ["Average Rank", "Film", "Year"]
output_df = pd.DataFrame(columns=columns)

html_page = requests.get(url).text
data = BeautifulSoup(html_page, "html.parser")

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

count = 0
for row in rows:
    if count < 50:
        col = row.find_all('td')
        if len(col) > 0:
            #print(f"col {count}: {col}")
            data_dict = {"Average Rank": col[0].contents[0],
                        "Film": col[1].contents[0],
                        "Year": intr(col[2].contents[0])}
            current_df = pd.DataFrame(data_dict, index=[0])

            # To prevent FutureWarnings, assign copy of current df if output_df is empty
            if output_df.empty:
                output_df = current_df.copy()
            else:
                output_df = pd.concat([output_df, current_df], ignore_index = True)
            count = count + 1
    else:
        break

# Save output to CSV
print(output_df)
output_df.to_csv(target_output_csv_file)
print(f"Saved CSV output to {target_output_csv_file}")

# Save output to DB
conn = sqlite3.connect(target_db_name)
output_df.to_sql(target_db_table_name, conn, if_exists='replace', index=False)
conn.close()
print(f"Saved DB output to {target_db_name}")
