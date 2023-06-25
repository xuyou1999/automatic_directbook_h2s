import requests
from bs4 import BeautifulSoup
import time
import sys

def get_regi_list(last_time):
    url = "the url of the housing list"
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
                if new_price <= 800: # change this to your desired price
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

def send_message(msg):
    TOKEN = "your__token"
    chat_id = "your_chat_id"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    print(requests.get(url).json()) # this sends the message

if __name__ == "__main__":
    last_time = time.time()
    while True:
        try:
            last_time = get_regi_list(last_time)
            time.sleep(12)
        except Exception as e:
            time.sleep(12)