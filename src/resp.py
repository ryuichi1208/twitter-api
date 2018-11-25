import config
from requests_oauthlib import OAuth1Session
import datetime, time

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

res = twitter.get(url)

limit = res.headers['x-rate-limit-remaining']
reset = res.headers['x-rate-limit-reset'] 
sec = int(res.headers['X-Rate-Limit-Reset']) - time.mktime(datetime.datetime.now().timetuple())

print ("limit: " + limit)
print ("reset: " +  reset)
print ('reset sec:  %s' % sec)
