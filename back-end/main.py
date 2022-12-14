import requests
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from keys import API_BEARER_TOKEN

tweetUrl = 'https://api.twitter.com/1.1/search/tweets.json?q='
profileUrl = 'https://api.twitter.com/1.1/users/lookup.json?screen_name='

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {API_BEARER_TOKEN}'
}

app = Flask(__name__)
api = Api(app)
cors= CORS(app, resources={r'/api/*': {'origins:': '*'}})

@app.route('/api/tweets/handle_search/<handle>', methods=['GET'])
def search_tweets_handle(handle):
    response = requests.get(tweetUrl+'from:'+handle+'&count=10', headers=headers).json()
    return response

@app.route('/api/tweets/keyword_search/<keyword>', methods=['GET'])
def search_tweets_keyword(keyword):
    response = requests.get(tweetUrl+keyword+'&count=10', headers=headers).json()
    return response

@app.route('/api/tweets/random/<handle>', methods=['GET'])
def search_tweets_random(handle):
    response = requests.get(tweetUrl+'from:'+handle, headers=headers).json()
    return response

@app.route('/api/profiles/<screen_name>', methods=['GET'])
def search_profiles(screen_name):
    response = requests.get(profileUrl+screen_name, headers=headers).json()
    return response

# @app.errorhandler(404)
# def not_found():
#     """Page not found."""
#     return make_response(render_template("404.html"), 404)

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000