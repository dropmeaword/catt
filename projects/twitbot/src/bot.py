#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
from pprint import pprint
import time
from random import randint
import os


CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

api = None

def connect():
	global api
	print "Connecting to the twitter API"
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

def search():
	global api
	twts = api.search(q="Hello World!")
	#pprint(twts[0])
	print "*"*80
	print twts[0].text
	# for t in twts:
	# 	pprint( t )

def mentions():
	mentions = api.mentions_timeline(count=1)
	if mentions:
		for m in mentions:
			print(m)
	else:
		print "No mentions yet"

def tweetforever():
	filename=open('lines.txt','r')
	f=filename.readlines()
	filename.close()

	#print "number of lines: ", len(f)
	#print f[:2]
	#print f[9]

	mn = 0
	mx = len(f)-1
	idx = randint(mn, mx)
	mytweet = f[idx]
	print mytweet

	mypic = "images/{0}.jpg".format( randint(0,696) )

	print mypic

	#api.update_status(status= mytweet)

	api.update_with_media(filename=mypic,status= mytweet, lat=63.631050 , long=-19.607225)

	# for line in f:
	#      api.update_status(status=line)
	#      print line
	#      time.sleep(1800) # Sleep for 30 mintues

def main():
	connect()
	while 1:
		tweetforever()
		time.sleep( randint(500, 3600))
	#search()
	#mentions()

if __name__ == "__main__":
	main()
