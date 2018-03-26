# -*- coding: utf-8 -*-
"""

@author: noura
"""
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pprint
import requests
from urllib import request
import json
import tkinter as tk
from tkinter import filedialog
from tkinter import *

# Variables that contains the user credentials to access Twitter API
access_token = "1464919340-4OHUBQdSJjTFG8LqMPmstkWPj0qPlemiQic4FmV"
access_token_secret = "8MdNlE3Q9N1NCoj9XfsiZaws43dJXoI0UMnoEGn723pkz"
consumer_key = "eKytO5h04YQhqwczDEXc0ubay"
consumer_secret = "WktfrnSWTSzBKwEoiooAPIQ11SAb09yjfsIO3KcClYRQsgb36b"
# This is a basic listener that just prints received tweets to stdout.

hashtag = 'google'
path = ''

def browse():
    global path
    path = filedialog.askdirectory()
    print(path)
    return path

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
                print(path)
                request.urlretrieve(img_url, str(path+'/{}').format(img_url[-19:]))
        return True
    
           

    def on_error(self, status):
        print(status)

def retrieveTweets():
    global hashtag
    hashtag = hashtagFromUser.get()
    global var
    if(str(var.get())== '1'):
        if __name__ == '__main__':
            # This handles Twitter authetification and the connection to Twitter Streaming API
            l = StdOutListener()
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            stream = Stream(auth, l, async=True)

            # This line filter Twitter Streams to capture images from hashtags.
   
            stream.filter(track=['#'+hashtag])
    elif(str(var.get())== '2'):
        print('not implemented')
        

var = 1
master = Tk()
var = IntVar()
master.geometry("340x130")
master.title("Hashtagpicsdownloader")
Label(master, text="#").grid(row=0,pady=5, column=0)
hashtagFromUser = Entry(master)
hashtagFromUser.grid(row=0, column=1, pady=2)
Button(master, command=retrieveTweets, text='Download Images').grid(row=12, column=2, sticky=W, pady=4)
Button(master, command=browse, text='Select Download Folder').grid(row=12, column=1, sticky=W, pady=4)
Radiobutton(master, text="Streaming", variable=var, value=1).grid(row=9, column=1, sticky=W, pady=4)
Radiobutton(master, text="old tweets", variable=var, value=2).grid(row=9, column=2, sticky=W, pady=4)
mainloop()

