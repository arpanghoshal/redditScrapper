from redditScrapper.firstThreeTitles import getFirstThreeTitles 
from flask import Flask,jsonify,request
app = Flask(__name__)



	
@app.route('/top_posts',methods=['GET'])
def query():
	subreddit = request.args.get('subreddit')
	ourFirstThreeTitles = getFirstThreeTitles(subreddit)
	ourResponse = {"response":{"code":200,"message":ourFirstThreeTitles}}
	return jsonify(ourResponse)
	
	
if __name__=='__main__':
	app.run(debug=True,host='localhost',port='80')
	

