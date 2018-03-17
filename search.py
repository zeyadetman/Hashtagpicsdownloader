import requests
import json

hashtag = "google"
url = "https://api.twitter.com/1.1/search/tweets.json"

querystring = {"q":str("%23"+hashtag),"count":"100"}

headers = {
    'Authorization': "OAuth oauth_consumer_key=\"Baun9jWdSbPoZFC4OjZBxLXoq\",oauth_token=\"176691300-joo3VAK7VHN8VOCC8ZsgIrAT83AG1dX0M0aPAjNy\",oauth_signature_method=\"HMAC-SHA1\",oauth_timestamp=\"1521286496\",oauth_nonce=\"CO6DrDE99fi\",oauth_version=\"1.0\",oauth_signature=\"HTAN8pitB1813MyvCn3GLLVQvQA%3D\"",
    'Cache-Control': "no-cache",
    'Postman-Token': "e6945e1f-5c0c-4880-b4e6-8f0a7c0751de"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

retrievedData = json.loads(response.text)['statuses']
dataLength = len(retrievedData)
print(retrievedData)