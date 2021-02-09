import requests
import csv
from bs4 import BeautifulSoup


NUM_PAGES = 50
NUM_BOOKS_PER_PAGE = 20
page_index = 1

# Data to collect per page.
title_links = []
prices = []  
id_numbers = []
cleaned_titles = []

# Data to collect per site.
all_titles = []
all_id_numbers = []
all_prices = []

# Traverse all pages.
for page in range(NUM_PAGES):
    title_links.clear()
    prices.clear()
    id_numbers.clear()
    cleaned_titles.clear()
    
    print('Data for page: ' + str(page_index) + '\n')
    
    if page_index != 1:
        page = requests.get('http://books.toscrape.com/catalogue/page-' + str(page_index) + '.html')
    else:
        page = requests.get('http://books.toscrape.com/')
        
    soup = BeautifulSoup(page.content, 'html.parser')    
    
    for link in soup.find_all('a'):
        if 'category' not in link.get('href'):
            title_links.append(link.get('href'))

    # Remove duplicates and clean first and last elements.
    titles = [] 
    for i in title_links: 
        if i not in titles: 
            titles.append(i) 
    titles = titles[1:-1]
    
    # Clean the titles.
    for x in titles:
        x = x.replace('catalogue', '')
        x = x.replace('index', '')
        x = x.replace('.html', '')
        x = x.replace('/', '')
        x = x.replace('-', ' ')
    
        cleaned_titles.append(x)

    # Clean 'noisy' data, such as page and .. strings.
    for x in cleaned_titles:      
        if 'page' in x or '..' in x:
            cleaned_titles.remove(x)  
    titles.clear()

    # Seperate titles from their id numbers.
    for x in cleaned_titles:
        y = x.split("_", 1)
        title = y[0]
        id_number = int(y[1])
        id_numbers.append(id_number)
        titles.append(title)

    # Find and clean prices.
    for p in soup.find_all('p'):
        prices.append(p.string)
    prices = [x for x in prices if x is not None]

    print(prices)
    print('\n')
    print(titles)
    print('\n')
    print(id_numbers)
    print('\n')

    all_titles.extend(titles)
    all_prices.extend(prices)
    all_id_numbers.extend(id_numbers)
    page_index += 1 

# Write to CSV
title_row = ['Book ID','Book Title', 'Book Price']

with open('book_titles.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(title_row)
    for id_number, title, price in zip(all_id_numbers, all_titles, all_prices):
        writer.writerow([id_number, title, price])
