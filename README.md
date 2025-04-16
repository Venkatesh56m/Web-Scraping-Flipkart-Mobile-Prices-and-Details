Project Overview: Flipkart Mobile Scraper
This Python project uses web scraping techniques to extract data from Flipkart’s website. Specifically, it scrapes information about mobile phones listed under ₹50,000. The data extracted includes:

Product Name

Price

Description

Customer Ratings

The script uses the requests library to fetch the web pages, and BeautifulSoup from bs4 to parse and extract the relevant information. Finally, the data is saved in a CSV format using the pandas library, which can be used for analysis or further processing.

Key Components:
Requests:

The script makes HTTP requests to Flipkart’s search result pages to retrieve HTML content.

BeautifulSoup:

BeautifulSoup is used to parse the HTML and navigate through the elements to extract the desired data (e.g., product names, prices, reviews).

Pandas:

pandas is used to organize the scraped data into a structured DataFrame. The data is then saved as a CSV file.

How It Works:
Request Pages:

The script sends a request to the Flipkart URL for mobiles under ₹50,000, appending the page number to scrape data from multiple pages.

Parse HTML:

BeautifulSoup processes the HTML of the page to find the elements containing the product details. It looks for specific HTML tags and class names that correspond to the product names, prices, descriptions, and reviews.

Extract Data:

The relevant information is extracted using BeautifulSoup's find_all() method, which finds all occurrences of a particular HTML element with the specified class names.

Store Data:

The extracted data is stored in four lists: Names, Prices, Desc, and Reviews.

Handle Length Mismatch:

The script ensures that all lists have the same length by trimming them to the shortest length. This prevents errors during DataFrame creation if there’s a mismatch in the number of items.

Create DataFrame:

The pandas library is used to create a DataFrame from the lists, where each list represents a column of the table.

Save to CSV:

The DataFrame is saved as a CSV file, allowing you to easily view and analyze the data in tools like Excel or other data analysis software.

Example Data:
The CSV will contain data like this:


Product Name	Product Prices	Product Description	Product Ratings
Apple iPhone 13	₹44,999	128 GB ROM, 6.1-inch Display, 12MP+12MP Camera	4.6
Samsung Galaxy S24	₹47,999	256 GB ROM, 6.7-inch Display, 50MP Camera	4.5
OnePlus
