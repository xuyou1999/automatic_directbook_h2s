import requests
from bs4 import BeautifulSoup
import time
import sys

def get_regi_list(last_time, budget, cities):
    url = get_url(cities)
    response = requests.get(url)
    msg = ""

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        regi_list = soup.find('div', class_='regi-list')
        if regi_list:
            items = regi_list.find_all('div', class_='regi-item d-flex flex-wrap')
            for item in items:
                regi_info = item.find('ul', class_='regi-info')
                places = regi_info.find_all('span')
                place_str = ''
                for place in places:
                    place_str += place.text
                    place_str += ' '
                price = item.find('div', class_='price regularbold')
                new_price = float(price.text.replace('€', '').replace(',', ''))
                if new_price <= budget:
                    print(new_price)
                    msg += f"Found a room that is {new_price} euros in "
                    msg += place_str
                    room_url = item.get('data-url')
                    msg += f"{room_url}\n"
        else:
            print("No 'regi-list' div found.")
    else:
        print(f"Request failed with status code: {response.status_code}")
        msg += f"Request failed with status code: {response.status_code}\n"
    
    if msg != "":
        current_time = time.time()
        if current_time - last_time > 120: # change this to your desired time, meaning if the last message was sent more than 2 minutes ago, send a new message
            send_message(msg)
            last_time = current_time

    return last_time

def get_url(cities):
    maps = {
        'Amsterdam': '24',
        'Arnhem': '320',
        'Capelle aan den IJssel': '619',
        'Delft': '26',
        'Den Bosch' : '28',
        'Den Haag': '90',
        'Den Bosch': '110',
        'Dordrecht': '620',
        'Eindhoven': '29',
        'Groningen': '545',
        'Haarlem': '616',
        'Helmond': '6099',
        'Maastricht': '6090',
        'Nijmegen': '6217',
        'Rotterdam': '25',
        'Rijswijk': '6224',
        'Sittard': '6211',
        'Tilburg': '6093',
        'Utrecht': '27',
        'Nieuwegein': '6051',
        'Zeist': '6145',
        'Zoetermeer': '6088'
    }
    if len(cities) == 1:
        city_para = f"{maps[cities[0]]}"
    else:
        city_para = f"{maps[cities[0]]}"
        for city in cities[1:]:
            city_para += f"%2C{maps[city]}"
    url = f"https://holland2stay.com/residences.html?available_to_book=179&city={city_para}&product_list_limit=30&product_list_order=price"
    return url

def send_message(msg):
    TOKEN = "your_token"
    chat_id = "your_chat_id"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    print(requests.get(url).json()) 

if __name__ == "__main__":
    budget = 2000
    cities = ['Amsterdam', 'Eindhoven']
    last_time = time.time() - 130
    while True:
        try:
            last_time = get_regi_list(last_time, budget, cities)
            time.sleep(12)
        except Exception as e:
            time.sleep(12)