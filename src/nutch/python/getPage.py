import requests
import logging
import json
import urllib
import base64
import http.client
import configparser
from tweepy import *
import python_http_client

from io import BufferedWriter

from urllib.parse import urlencode
from base64 import b64encode

config = configparser.RawConfigParser()
config.read("settings.properties","utf-8")

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

EMAIL = 'wpjunior@br.ibm.com'
PASSWORD = 'kyuhhud6'

URL = 'https://agile-ibm.mybluemix.net/'

USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.14) Gecko/2009082707 Firefox/3.0.14 (.NET CLR 3.5.30729)"
GITHUB_URL = "https://api.github.com/search/repositories?q=Reactive"
HITHUB_HOST = "api.github.com"
TWITTER_HOST = "api.twitter.com"
TWITTER_AUTH_URL = "https://api.twitter.com/oauth2/token"
TWITTER_URL = "https://api.twitter.com/1.1/search/tweets.json?q="

def requestGitHub(endPointUrl):
    response = requests.session().get(endPointUrl)
    json_data = json.loads(response.text)
    return json_data
    
def fetchTimelineTweet(endPointUrl, bearerToken):
    
    headers = {'Authorization' : 'Bearer '+bearerToken}
    response = requests.session().get(endPointUrl,headers=headers)
    json_data = json.loads(response.text)
    return json_data
    
def requestBearerToken(endPointUrl):
    
    encodedCredentials = encodeKeys(config.get('Section','consumerKey'), config.get('Section','consumerSecret'))
    
    headers = {
        'Host': TWITTER_HOST,
        'User-Agent': USER_AGENT,
        'Content-Length':str(len(encodedCredentials)),
        'Content-Type' : 'application/x-www-form-urlencoded;charset=UTF-8', 
        'content-type' : 'application/json',
        'Authorization' : 'Basic '+encodedCredentials}
    
    #version = 3  # we could also use client.version(3)
    #client = python_http_client.Client(host=endPointUrl,
    #                               request_headers=headers,
    #                               version=version)
    # GET collection
    
    #response = client.post()

    auth = OAuthHandler(config.get('Section','consumerKey'), config.get('Section','consumerSecret'))
    api = API(auth)
    
    for tweet in Cursor(api.search, 
                        q = "google",
                        since_id = "2014-02-14",
                        lang = "en").items():
        print(tweet)
    
    response = requests.session().post(endPointUrl,headers=headers)
    
    print(response.status_code)
    print(response.headers)
    print(response.body)
    
    json_data = json.loads(response.text)
    return json_data

def encodeKeys(consumerKey, consumerSecret):

    encodedConsumerKey = urllib.parse.quote(consumerKey)

    encodedConsumerSecret = urllib.parse.quote(consumerSecret)

    fullKey = encodedConsumerKey + ":" + encodedConsumerSecret
    encodedBytes = b64encode(fullKey.encode('utf-8'));
    
    return encodedBytes.decode('utf-8')

def main():
    # Start a session so we can have persistant cookies
    githubResults = requestGitHub(GITHUB_URL).get('items')
    
    projCounts = int(config.get('Section','numberOfProjectsToList'))
    
    githubProjects = json.dumps({})
        
    githubProjectWithTweets = json.dumps({})
        
    githubRetrieveFields = config.get('Section','githubRetrieveFields').split(',')
    
    allFields = (githubRetrieveFields[0]=="*")
    
    for items in githubResults: 
    
        githubProject = items
        
        term = githubProject.get(config.get('Section','searchTweetsByGithubField'))

        if (term!=""):
            # searching for tweets
            jsonTweets = fetchTimelineTweet(TWITTER_URL+term, requestBearerToken(TWITTER_AUTH_URL))
            
            # adding the tweets results to the github project
            githubProject.put("recent_tweets", jsonTweets)

        # all fields, add it all to the github project
        if (allFields):
            githubProjectWithTweets = items
        else:
            # feed the github project with selected fields
            for field in githubRetrieveFields: 
                githubProjectWithTweets.put(field, githubProject.get(field))
        
        githubProjects.append(config.get('Section','githubProjectsList'), githubProjectWithTweets);
        
        # print the output of the retrived github project within tweets 
        print(githubProjects)
        
        

if __name__ == '__main__':
    main()