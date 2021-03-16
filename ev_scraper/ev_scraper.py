import requests
import csv
import helper
import sys
import os.path
from bs4 import BeautifulSoup


# Data to extract.
header = ['Model', 'Price UK', 'Price Netherlands', 'Price Germany',
          'Availability UK', 'Availability Netherlands', 'Availability Germany',
          'City - Cold Weather', 'Highway - Cold Weather', 'Combined - Cold Weather',
          'City - Mild Weather', 'Highway - Mild Weather', 'Combined - Mild Weather',
          'Acceleration 0 - 100 km/h', 'Top Speed', 'Electric Range',
          'Total Power', 'Total Torque', 'Drive']

# Change this value to continue appending to ev_data.csv from where the script was terminated.
# index = # of extracted car untill now + 1.
global_index = 140

page = requests.get('https://ev-database.org/')       
soup = BeautifulSoup(page.content, 'html.parser')

# Write CSV.
if not os.path.isfile('ev_data.csv'):
    with open('ev_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    
# Clear every link that it's not a car reference.
ev_links = []
for link in soup.find_all('a'):
    if 'compare' not in link.get('href') and '/car/' in link.get('href'):
        ev_links.append(link.get('href'))

# Remove duplicates and get first proxy.
ev_links = list(dict.fromkeys(ev_links))
new_proxy = helper.add_proxy()


def main(new_proxy):
    global global_index
    global header

    # For every EV    
    for car_link in ev_links:              
        specs_list = []
        new_user_agent = helper.change_user_agent()  

        if global_index == len(ev_links):
            sys.exit()
        try:
            page = requests.get('https://ev-database.org' + ev_links[global_index], proxies=new_proxy, timeout=8, headers=new_user_agent)
            if(page.status_code != 200):
                print('\nRequest blocked. Trying a new proxy...')
                new_proxy = helper.add_proxy()
                main(new_proxy)
        except:
            print('\nThis proxy dont work. Trying a new one...')
            new_proxy = helper.add_proxy()
            main(new_proxy)

        soup = BeautifulSoup(page.content, 'html.parser')

        # Get model name.
        model_name = soup.find('h1')

        # Check for matching pattern.
        availability_found = False
        real_range_estimation_found = False
        for x in soup.find_all('h2'):
            if x.string is None or 'Availability' in x.string:
                availability_found = True
                
            if x.string is None or 'Real Range Estimation' in x.string:
                real_range_estimation_found = True

            if x.string is not None and 'Concept Status' in x.string:
                availability_found = False
                real_range_estimation_found = False
                break
                
        if availability_found == False or real_range_estimation_found == False:
            print('\nCar not for extraction! Skipping...')
            global_index += 1
            continue
        
        # Removing unwanted tables.
        table_index = 1
        for table in soup.find_all('table'):
            if table_index > 6:
                table.extract()
            table_index+=1

        # Get the rest.
        td_info = [td.string for td in soup.find_all('td') if td.string is not None]
        header_list = []
        specs_list = []
                                    
        for x in td_info:
            x = x.replace('\t', '')
            if x not in header and '*' not in x:
                specs_list.append(x)

        # Post-cleaning and casting.
        cleaned_specs = []
        for spec in specs_list:
            if 'km' in spec or '\h' in spec or 'Nm' in spec or '£' in spec or '€' in spec or 'sec' in spec:                
                spec = spec.replace('£', '').replace('€', '').replace('km', '').replace('/h', '').replace('Nm', '').replace('sec', '').replace(',', '.')
                spec = spec.replace(' ', '')                                 
                spec = float(spec)            
            elif 'kW' in spec:
                spec = int(spec[:-12])
                
            cleaned_specs.append(spec)
    
        cleaned_specs.insert(0, model_name.string)
        print('\n Car(' + str(global_index + 1) + ') specs:\n')
        print(cleaned_specs)
                    
        with open('ev_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(cleaned_specs)
            
        global_index += 1 
        helper.delay_request()
        # Debuging break
        #break
      

main(new_proxy)
