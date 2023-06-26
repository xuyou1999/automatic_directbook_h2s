# Holland2Stay Direct Booking Detector

## Overview
This application continually checks for available "direct booking" properties on the Holland2Stay website, based on your personal preferences. If a property matching your criteria becomes available, the program instantly notifies you via Telegram.

## Setup Instructions

### Prerequisites
- Basic coding abilities
- A Python-execution platform (I recommend PythonAnywhere by Anaconda. Note: A subscription to the 6 EUR plan is required for cloud execution)
- A Telegram account

### Setup Steps
1. Open Telegram, search for @BotFather, and send the "/start" message.
2. Start a new bot by sending "/newbot" and follow the on-screen instructions to set a bot name and username.
3. After setting up your bot, make a note of the provided token (important for setup).
4. Find your bot (using the username you've just created) in Telegram, then press the “Start” button or send a "/start" message.
5. In a new browser tab, navigate to `https://api.telegram.org/bot{yourtoken}/getUpdates`, replacing `{yourtoken}` with your bot token, and hit enter.
6. Locate the "id" - this is your chatID. Record this for later use.
7. Open the `auto_detect.py` file in an editor (like VS Code).
8. Customize the script:
    - On line 80, replace `TOKEN` with your Telegram bot token.
    - On line 81, replace `your_chat_id` with your Telegram chat ID (include the quotes, like `"1234567890"`).
    - On line 86, set the `budget` parameter to your maximum preferred price.
    - On line 87, fill the `cities` parameter with a list of cities you're interested in (e.g., `["Amsterdam", "Delft"]`).
9. Set up and run the Python file on PythonAnywhere to execute it continuously (note: this requires a subscription). Alternatively, you can directly run the program on your device, but ensure it remains active during your absence.
10. As soon as properties matching your criteria are available, you will receive a message on Telegram.

### Advanced Settings
- The program is currently configured to check the website every 12 seconds. To change this interval, modify the values on lines 92 and 94 (time is in seconds). Remember to execute responsively, and note that faster scraping can consume more resources if running in the cloud.
- The program also waits 2 minutes between each message to avoid excessive notifications. You can adjust this interval on line 39.

For any inquiries, feel free to contact me at xuyou1999@icloud.com.
