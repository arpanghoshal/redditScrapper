import requests
from bs4 import BeautifulSoup

def getFirstThreeTitles(subreddit,num):
	URL = "https://www.reddit.com/r/"+subreddit+"/top"
	
	headers = {'User-Agent':'Mozilla/5.0'}
	response=requests.get(URL,headers=headers)
	
	soup=BeautifulSoup(response.content,'lxml')
	
	#loops cannot be used- reddit restrictions
	i=0
	titles = []
	while(i<num):
		title =soup.select('._eYtD2XCVieq6emjKBH3m')[i].get_text()
		titles.append(title)
		i+=1
	return titles
	
"""

Can't use BeautifulSoup in html or any other format because of requests.exceptions.ConnectionError
https://www.reddit.com/robots.txt shows which requests are disallowed.


"""
