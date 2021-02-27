import requests
from bs4 import BeautifulSoup

def getFirstThreeTitles(subreddit):
	URL = "https://www.reddit.com/r/"+subreddit+"/top"
	
	headers = {'User-Agent':'Mozilla/5.0'}
	response=requests.get(URL,headers=headers)
	
	soup=BeautifulSoup(response.content,'lxml')
	
	#loops cannot be used- reddit restrictions
	title1 =soup.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()
	title2 =soup.select('._eYtD2XCVieq6emjKBH3m')[1].get_text()
	title3 =soup.select('._eYtD2XCVieq6emjKBH3m')[2].get_text()
	
	
	return [title1,title2,title3]
	
"""

Can't use BeautifulSoup in html or any other format because of requests.exceptions.ConnectionError
https://www.reddit.com/robots.txt shows which requests are disallowed.


"""
