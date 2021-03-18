# This script handles techniques to make the scraper less noticable.
import random
import time
import requests
from bs4 import BeautifulSoup


def change_user_agent():
    # User agent's pool.
    user_agent_list = [
        'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3' ]
    
    #print('\nCurrent user agent: \n' + random.choice(user_agent_list) + '\n')
    user_agent = {
        'User-Agent': random.choice(user_agent_list)
    }
    return user_agent 


# Purposely slowing down scraper with random intervals, making it less noticable. Minimum 10 seconds.
def delay_request():
    seconds_delay = random.randint(0,10)
    seconds_delay += 10
    time.sleep(seconds_delay)
    #print('\nSeconds delayed before the next request: ' + str(seconds_delay))


def add_proxy():
    page = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Get every 8 elements. (Proxy IP's)
    td_elements = soup.find_all('td')
    proxy_ip_list = td_elements[::8]

    # Cut last 20 elements, since they are not ip's.
    proxy_ip_list = proxy_ip_list[:-20]

    # Same for port.
    port_list = td_elements[1::8]
    port_list = port_list[:-20]

    # Clean and stringify.
    proxy_list_cleaned = []
    port_list_cleaned = []
    proxy_ip_list = [str(x) for x in proxy_ip_list if x is not None]
    port_list = [str(x) for x in port_list if x is not None]
        
    for x in proxy_ip_list:
        x = x.replace('<td>', '').replace('</td>', '')
        proxy_list_cleaned.append(x)

    for x in port_list:
        x = x.replace('<td>', '').replace('</td>', '')
        port_list_cleaned.append(x)
   
    # Pick random proxy and it's respective port.
    random_idx = random.randint(0, len(proxy_ip_list)-1)
    random_proxy = proxy_list_cleaned[random_idx]
    random_port = port_list_cleaned[random_idx]
   
    # Create dictionary for the scraper to use.
    proxy_str = random_proxy + ':' + random_port
    
    dict_result = {}
    dict_result['http'] = proxy_str
    dict_result['https'] = proxy_str
    print('\nNew proxy:')
    print(dict_result['http'])
    return dict_result
