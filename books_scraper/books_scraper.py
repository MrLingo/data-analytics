import requests
import csv
from bs4 import BeautifulSoup


NUM_PAGES = 50
NUM_BOOKS_PER_PAGE = 20
page_index = 1

# Data to collect per site.
all_titles = []
all_id_numbers = []
all_prices = []


for page in range(NUM_PAGES):
    titles = []
    prices = []  
    id_numbers = []
    cleaned_titles = []
    
    print('Data for page: ' + str(page_index) + '\n')   
    if page_index != 1:
        page = requests.get('http://books.toscrape.com/catalogue/page-' + str(page_index) + '.html')
    else:
        page = requests.get('http://books.toscrape.com/')
        
    soup = BeautifulSoup(page.content, 'html.parser')    

    # Get all title links.
    titles = [link.get('href') for link in soup.find_all('a') if 'category' not in link.get('href')]

    # Remove duplicates and clean first and last elements.
    titles = list(dict.fromkeys(titles))
    titles = titles[1:-1]
    
    # Clean the titles.
    for x in titles:
        x = x.replace('catalogue', '').replace('index', '').replace('.html', '').replace('/', '').replace('-', ' ') 
        cleaned_titles.append(x)

    # Clean 'noisy' data, such as 'page' and '..' strings.
    for x in cleaned_titles:      
        if 'page' in x or '..' in x:
            cleaned_titles.remove(x)  
    titles.clear()

    # Separate titles from their id numbers.
    for x in cleaned_titles:
        y = x.split("_", 1)
        title = y[0]
        id_number = int(y[1])
        id_numbers.append(id_number)
        titles.append(title)

    # Find and clean prices.
    prices_temp = []
    for p in soup.find_all('p'):
        prices_temp.append(p.string)
    prices_temp = [x for x in prices_temp if x is not None]

    for price in prices_temp:
        price = float(price.replace('£', ''))
        prices.append(price)
            
    print(str(prices) + '\n')
    print(str(titles) + '\n')
    print(str(id_numbers) + '\n')

    all_titles.extend(titles)
    all_prices.extend(prices)
    all_id_numbers.extend(id_numbers)
    page_index += 1 

# Write to CSV
header = ['Book ID','Book Title', 'Book Price(£)']

with open('book_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for id_number, title, price in zip(all_id_numbers, all_titles, all_prices):
        writer.writerow([id_number, title, price])
