from redditScrapper.firstThreeTitles import getFirstThreeTitles 
from flask import Flask,jsonify,request
from werkzeug import exceptions

app = Flask(__name__)


@app.errorhandler(exceptions.BadRequest)
def error_400(e):
    return jsonify('Bad Request'), 400

@app.errorhandler(exceptions.NotFound)
def error_404(e):
    return jsonify('Not Found'), 404

@app.errorhandler(exceptions.MethodNotAllowed)
def error_405(e):
    return jsonify('Method Not Allowed'), 405
    
@app.errorhandler(exceptions.InternalServerError)
def error_500(e):
    return jsonify('Internal Server Error'), 500

	
@app.route('/top_posts',methods=['GET'])
def query():
	subreddit = request.args.get('subreddit')
	num = 3 #no. of titles
	ourFirstThreeTitles = getFirstThreeTitles(subreddit,num)
	ourResponse = {"response":{"code":200,"message":ourFirstThreeTitles}}
	return jsonify(ourResponse), 200
	
	
if __name__=='__main__':
	app.run(debug=True,host='localhost',port='80')
	

