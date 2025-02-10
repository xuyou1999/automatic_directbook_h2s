# Holland2Stay Direct Booking Detector

## **Important Notice: Project Status**

**This repository is currently not maintained or functional.** However, I would like to take a moment to explain the background, vision, and reasoning behind this project.

### **Background and Vision**
The initial goal of this project was to promote equal access to housing resources in the Netherlands, particularly in response to the challenging rental market. I observed that on Mandarin-speaking platforms like RedNote (小红书), some individuals were using bots to secure housing and charging exorbitant commissions for their services. This practice creates an unfair disadvantage for those without coding experience or the financial means to pay for such assistance—**a practice that also violates the terms of service of most housing platforms.**

To address this imbalance, I decided to develop and open-source similar tools, as the underlying technology is publicly available. My aim was to level the playing field and empower individuals to compete fairly in the housing market.

### **The Current Landscape**
I am encouraged to see that many others who share the same values and vision have begun open-sourcing similar projects on social media and open-source platforms. This collective effort has helped counteract unfair practices by fostering competition and transparency.

Additionally, housing platforms like Holland2Stay have implemented more advanced measures to prevent the use of automated bots, making the rental market fairer for all seekers. As a result, I believe this project no longer needs active support or maintenance. Continuing to do so would also impose increasing deployment complexity and workload, which is no longer justified.

### **Future of This Project**
While this project is no longer actively maintained, it will remain **open-source and freely available** for anyone to use, modify, or build upon. I encourage others to continue developing solutions that promote fairness and combat exploitative practices (such as those by "黄牛" or scalpers).

### **Final Note**
I wish you the best of luck in your housing search! If you have any questions or ideas, feel free to reach out or contribute to the project.

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
    - Go to `Files` tab, upload the file `auto_detect_py`
    - Go to `Tasks` tab, create an Always-on Task with command `python3.10 /home/{username}/auto_detect.py` by replacing `{username}` to your username
10. As soon as properties matching your criteria are available, you will receive a message on Telegram.

### Advanced Settings
- The program is currently configured to check the website every 12 seconds. To change this interval, modify the values on lines 92 and 94 (time is in seconds). Remember to execute responsively, and note that faster scraping can consume more resources if running in the cloud.
- The program also waits 2 minutes between each message to avoid excessive notifications. You can adjust this interval on line 39.

For any inquiries, feel free to contact me at xuyou1999@icloud.com.
