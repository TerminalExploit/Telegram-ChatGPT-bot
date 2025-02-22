<p align="left">
   <img src="https://img.shields.io/badge/Python-3.9+-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Selenium-4.9.0-blue" alt="Selenium Version">
  <img src="https://img.shields.io/badge/WebDriver-4.8.1-blue" alt="WebDriver Version">
  <img src="https://img.shields.io/badge/PythonTelegramBot-20.1-blue" alt="Python-Telegram-Bot Version">
   <img src="https://img.shields.io/badge/Version-v0.1-blue" alt="Version">
   <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
</p>

# Telegram ChatGPT Bot
This project is a Telegram bot that redirects your messages from a chat with the bot to the web version of ChatGPT and then returns the responses back to the chat. The bot works locally on your computer without using the ChatGPT API.

## Features
- Message redirection: Your messages from Telegram are sent to the ChatGPT web version, and the responses are returned to Telegram.
- Access protection: The bot is only accessible to authorized users with a unique 16-character code.
- Local operation: Does not require OpenAI's paid API; all processing is done via a local browser.
- Simple setup: Clear project structure for quick deployment.

# Requirements
To run the project, you need:

1. Python version 3.9 or higher.
2. **Google Chrome** version compatible with the installed ChromeDriver.
3. **ChromeDriver**, matching your Chrome version.
4. Installed dependencies from requirements.txt.
5. **Telegram bot**, created via BotFather.

### Project Structure
```
Telegram-ChatGPT-bot/
│
├── bot.py              # Main bot script
├── browser.py          # Module for managing the browser via Selenium
├── config.py           # Configuration file: token, access code, etc.
├── requirements.txt    # Project dependencies
└── README.md           # Project description

```

## Installation
1. **Clone the repository:**
```
git clone https://github.com/TerminalExploit/Telegram-ChatGPT-bot.git
cd Telegram-ChatGPT-bot
```

2. **Install dependencies:**
```
pip install -r requirements.txt
```

3. **Download and set up ChromeDriver:**
- Check your current Chrome version:
  Open Chrome and navigate to chrome://settings/help.
- Download the matching ChromeDriver version from the official site.
- Unzip the file and add the ChromeDriver path to your PATH environment variable, or save it in the project root directory.

4. **Set up the Telegram token:**
- Obtain the token from [BotFather](https://t.me/BotFather)
- Specify the token in the config.py file:
```
TELEGRAM_TOKEN = "your-token"
```

5. **Set up the access code:**
In config.py, define a 16-character access code:
```
ACCESS_CODE = "your-secret-code"
```
6. **Run the bot:**

Make sure all dependencies are installed and ChromeDriver is accessible. Start the bot:
```
python bot.py
```

## Proxy Configuration (Optional)
If you need a proxy to access ChatGPT:
  1. Install a Chrome extension for proxy management.
  2. Configure browser options in browser.py, adding the path to your extension:
```
options.add_extension('path_to_proxy_extension')
```

## Usage
1. Start the bot:
```
python bot.py
```
2. Open Telegram and send ```/start``` to the bot.
3. Enter your secret code using the command:
```
/setcode your-code
```
4. Start sending messages and receive responses from ChatGPT.

## Common Errors and Solutions
### Error: telegram.error.InvalidToken
- Ensure you have specified the correct token in config.py.
- Obtain a new token from BotFather and update it in the code.
### Error: ChromeDriver executable needs to be available
- Check if ChromeDriver is installed and matches your Chrome version.
- Ensure the ChromeDriver path is specified correctly.
### CAPTCHA verification issue on ChatGPT
- Log in to your OpenAI account manually via Chrome before running the bot.
- Make sure you are using the same Chrome profile for automation.
