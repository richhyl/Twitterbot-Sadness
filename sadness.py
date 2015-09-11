#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, random, json
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


with open('text.txt') as f:
   lines = f.readlines()

tweets_replied_to = set()

while True:
	search = api.search('#sadness')
	for search_result in search:
		if search_result.id in tweets_replied_to:
			continue

		tweets_replied_to.add(search_result.id)

		if search_result.in_reply_to_status_id != None:
			continue

		if  search_result.retweet != None:
			continue

		target_username = search_result.author.screen_name
		line = "@{} {} #dadjoke".format(target_username, random.choice(lines).strip())
		api.update_status(status=line, in_reply_to_status_id=search_result.id)
		print "Replying to '{}' with '{}'".format(search_result.text, line)
		time.sleep(5)#Tweet every 15 minutes()
	time.sleep(20)#Tweet every 15 minutes()
