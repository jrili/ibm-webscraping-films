# Webscraping Project: Most Highly-Ranked Films
_Instructions and dataset taken from IBM's [Python Project for Data Engineering](https://www.coursera.org/learn/python-project-for-data-engineering) from Coursera_

# Links
|     Item       |   Link   |
| -------------- | ---------|
|Course Link | [IBM: Python Project for Data Engineering (Coursera)](https://www.coursera.org/learn/python-project-for-data-engineering) |
| Webscraping Target | [100 Most Highly-Ranked Films](https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films) |
| Author's Course Completion Certificate|[Certificate](https://www.coursera.org/account/accomplishments/verify/TFH7N05KO7D3) |
| Author's Data Engineer Portfolio | [jrili/data-engineer-portfolio](https://github.com/jrili/data-engineer-portfolio) |

# Dataset Details
**[100 Most Highly-Ranked Films](https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films)** contains a collated list of films with the highest ranking as of 2023 September 02. The release date of the films in the list as of writing range from 1916 to 2020.

The ranking is based from five (5) poll-based and/or expert top 100 lists, namely ([Rotten Tomatoes](https://www.rottentomatoes.com/), [IMDB](https://www.imdb.com/), AFI, Empire, and Sight and Sound)

# Scenario
Consider that you have been hired by a Multiplex management organization to extract the information of the top 50 movies with the best average rating from the web link shared above.

- The information required is Average Rank, Film, and Year
- Save it to a CSV file
- Load the information to a database under the table with name `Top_50`.

# Prerequisite Steps
## 1. Install required libraries
```
python -m pip install -r requirements.txt
```

# Project Tasks

## 1. Analyze the HTML code for relevant information
1. Open the web page in a browser then locate the required table.
2. Right-click on the table and click `Inspect` or something similar, depending on what browser you are using.
![alt text](image.png)
3. This opens the HTML code for the page and takes you directly to the point where the definition of the table begins. Take note of this structure in preparation for webscraping, i.e. what tags to look for for each row.
![alt text](image-1.png)

## 2. Load the webpage for webscraping
Develop a script that loads the entire web page and parses the resulting text in HTML format. The `requests` and `BeautifulSoup` (`bs4`) packages will be useful here.

## 3. Scrape the required information
Develop a script that scrapes the Average Rank, Film, and Year of the Top 50 Highly-Ranked Films from the HTML code.

## 4. Storing the data
Store the scraped data into a CSV file. In addition, save the scraped data into a database.

# How to execute:
_(Tested in Python 3.13)_
```
python webscraping_movies.py
```

# Acknowledgements
## Course Instructors
- Ramesh Sannareddy
- Joseph Santarcangelo
- Abhishek Gagneja
## Course Offered By
* [IBM Skills Network](https://www.coursera.org/partners/ibm-skills-network)
