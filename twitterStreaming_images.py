# -*- coding: utf-8 -*-
"""

@author: noura
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pprint
from urllib import request

# Variables that contains the user credentials to access Twitter API
access_token = "1464919340-4OHUBQdSJjTFG8LqMPmstkWPj0qPlemiQic4FmV"
access_token_secret = "8MdNlE3Q9N1NCoj9XfsiZaws43dJXoI0UMnoEGn723pkz"
consumer_key = "eKytO5h04YQhqwczDEXc0ubay"
consumer_secret = "WktfrnSWTSzBKwEoiooAPIQ11SAb09yjfsIO3KcClYRQsgb36b"
# This is a basic listener that just prints received tweets to stdout.

#overwrite stream listener 
class StdOutListener(StreamListener):
    debug_file = open('debug.txt', mode = 'a')
    def on_data(self, data):
      
        data = json.loads(data)
        if('media' in data['entities']):
            media = data['entities']['media']
            for img in media:
                    
                img_url = img['media_url']
                print(img_url) #get image url 
                 #add your path here
                 # then download it to this path.
                request.urlretrieve(img_url, 'C:\\Users\\noura\\Desktop\\pics\{}'.format(img_url[-19:]))
        return True
    
            
            
            
            

    def on_error(self, status):
        print(status)



if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, async=True)

    # This line filter Twitter Streams to capture images from hashtags.
   
    stream.filter(track=['#PalmSunday'], languages=["en"])
