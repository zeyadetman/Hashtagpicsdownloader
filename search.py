import requests
import json
import tkinter as tk
from tkinter import filedialog
from tkinter import *

hashtag = 'google'
def setHashtag():
    hashtag = hashtagFromUser.get()

def retrieveTweets():
    url = "https://api.twitter.com/1.1/search/tweets.json"

    querystring = {"q":hashtag,"count":"100"}

    headers = {
        'Authorization': "OAuth oauth_consumer_key=\"Baun9jWdSbPoZFC4OjZBxLXoq\",oauth_token=\"176691300-joo3VAK7VHN8VOCC8ZsgIrAT83AG1dX0M0aPAjNy\",oauth_signature_method=\"HMAC-SHA1\",oauth_timestamp=\"1521293558\",oauth_nonce=\"zudvlTt1EaQ\",oauth_version=\"1.0\",oauth_signature=\"DZZSLw9tKEBoI7aDMN%2BTK9QhNhk%3D\"",
        'Cache-Control': "no-cache",
        'Postman-Token': "5b254565-165f-4f15-a0f4-9b411369becf"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    retrievedData = json.loads(response.text)['statuses']
    dataLength = len(retrievedData)
    print(dataLength)

def browse():
    path = filedialog.askdirectory()
    print(path)

master = Tk()
master.geometry("300x140")
master.title("Hashtagpicsdownloader")
Label(master, text="Hashtag").grid(row=0,pady=5, column=0)
hashtagFromUser = Entry(master)
hashtagFromUser.grid(row=0, column=1, pady=2)
Button(master, command=setHashtag, text='Ok').grid(row=0, column=5, sticky=W, pady=4)
Button(master, command=retrieveTweets, text='Download Images').grid(row=10, column=1, sticky=W, pady=4)
Button(master, command=browse, text='Select Download Folder').grid(row=9, column=1, sticky=W, pady=4)
mainloop()
