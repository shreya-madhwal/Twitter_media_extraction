
from flask import Flask,redirect,url_for,render_template,request
import tweepy

consumer_key = "8fqcZBhHRJ2dP4cgSjqBWmR9A" 
consumer_secret = "pesGHBY9Vj0tBeEQag5rokeeCBJd0vjbqNFKtzb6e2ZFq8qxFN"
access_key = "1466114130818052106-eaopfN0JHitHaAlYjJqD9GiAd0A2LA"
access_secret = "m6v6bCSLUT3gwll7DrBSP9OfTR60942vdDu0WI7J1TSPc"


app=Flask(__name__)

def get_auth():
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
    api = tweepy.API(auth)

    return api

def imagesFromHashtag(hashtag):
    api=get_auth()
    images=[]
    for tweets in tweepy.Cursor(api.search_tweets,q=hashtag,count=150).items(200):
        #print(tweets.entities)
        if 'media' in tweets.entities:
            k=tweets.entities['media'][0]['media_url']
            images.append(k)
    
    return images                                  
        

@app.route("/",methods=["POST","GET"])

 
@app.route("/login",methods=["POST","GET"])


def main_login():
    if(request.method=="POST"):
        form_data=request.form["nm"]
        image_url=imagesFromHashtag(form_data)
        return render_template('home.html',sent=image_url)
    else:
        return render_template("/login.html")

@app.route('/about_us')
def about_us():
    return render_template('/about_us.html')

@app.route('/contact_us')
def contact_us():
    return render_template('/contact_us.html')

if __name__== '__main__':
    app.run(debug=True) 




