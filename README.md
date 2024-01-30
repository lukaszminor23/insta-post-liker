# Instagram Post Liking Bot

This is a simple Python script that I wrote during an online Python bootcamp: 100 days of code b y Angela Yu.
The script is using the Selenium library to automate post liking of a specified Instagram profile. On the course,
the script was supposed to follow all the followers of an account and I modified it to like all posts instead.


## Prerequisites

- Python 3.11
- Selenium library
- Chrome browser

## Installation

Clone the repository:

    git clone https://github.com/lukaszminor23/instagram-follower-bot.git


## Install dependencies:
    pip install selenium

## Configuration
Edit the script (main.py) and update the following variables with your Instagram account information:
- ACCOUNT = "instagram account name, that you want to like"
- EMAIL = "your_instagram_email@example.com"
- PASSWORD = "your_instagram_password"

## Usage
Run the script:

    python main.py
The script will log in to your Instagram account and automatically like the posts on the specified account.

## Disclaimer
This script interacts with Instagram's platform, and any misuse or abuse may violate Instagram's terms of service.
Use it responsibly and at your own risk.

## Acknowledgements
Special thanks to Angela Yu for teaching me how to use the Selenium library and Python in general.

Link to the course:
https://www.udemy.com/course/100-days-of-code