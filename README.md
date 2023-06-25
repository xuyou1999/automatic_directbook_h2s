# Automatic Direct Booking Detector for Holland2Stay

## Overview
This program monitors the "book directly" properties on the Holland2Stay website according to your preferences. When such properties become available, it instantly sends a notification to your Telegram account.

## Setup Instructions

### Prerequisites
- Basic coding skills (minimal)
- An online platform to execute the Python program (We recommend PythonAnywhere by Anaconda. Note: You'll need to subscribe to a 6 EUR plan to run this on Cloud)
- A Telegram account

### Steps
1. Launch Telegram and search for @BotFather.
2. Send the "/start" message to @BotFather.
3. Send another message "/newbot" and follow the instructions to set up a bot name and username.
4. After your bot is ready, make sure to note down the given token (this is crucial).
5. Search for your bot (using the username you just created) in Telegram, and then press the “Start” button or send a "/start" message.
6. Open a new browser tab and navigate to `https://api.telegram.org/bot_yourtoken_/getUpdates`, replacing `_yourtoken_` with your API token, then press enter.
7. Look for "id" - this is your chatID. Make sure to note it down.
8. Visit the Holland2Stay website, and set all the filters based on the properties you want to monitor.
9. Set "show" to "rent p/month".
10. Copy the URL of the page.
   - For reference, here are some URLs for specific locations:
     - Eindhoven: `https://holland2stay.com/residences.html?available_to_book=179&city=29&product_list_order=price`
     - Amsterdam: `https://holland2stay.com/residences.html?available_to_book=179&city=24&product_list_order=price`
     - Amsterdam + Eindhoven: `https://holland2stay.com/residences.html?available_to_book=179&city=24%2C26&product_list_order=price`
11. To monitor additional cities, determine the city code first and add "%2C" followed by the city code to the city parameter.
12. In the `auto_detect` python file, replace:
    - `url` with the copied URL.
    - `new_price` with the maximum price you want to monitor.
    - `TOKEN` with your Telegram bot token.
    - `chat_id` with your Telegram chat ID.
13. Set up this Python file on PythonAnywhere and create a task to make it run indefinitely. Note: You'll need a subscription for this functionality.

For any queries, feel free to contact me at xuyou1999@icloud.com.
