# Reddit Scrapper

This is a Python app built on a Flask framework for scrapping first 3 top titles of a subreddit topic.
For detail explanation refer to this blog. 
[How to create a bot to extract content from reddit with BeautifulSoup?](https://arpanghoshal.medium.com/how-to-create-a-bot-to-extract-content-from-reddit-with-beautifulsoup-4f528c339ab8) by Arpan Ghoshal

### Requirements
- Python3
- Flask
- BeautifulSoup4
- requests

### Installing dependencies
> $ pip3 install -r requirements.txt

### To run the application
> $ python3 app.py

To change the host or port, edit config in app.py 

#### If port is 80 (localhost) or 433, sudo (root) permisions are needed.
#### Currently, the app is running on development server. For production, run it on gunicorn server.

## Output
![Output Generated](https://github.com/arpanghoshal/redditScrapper/blob/main/output.jpg)

