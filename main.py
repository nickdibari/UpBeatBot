#! /usr/bin/python

# UpBeatBot
# Nicholas DiBari
# Twitter bot to tweet uplifting things

import bs4
import random
import requests
import twitter
import time

from auth_example import *

# PRE: N/A
# POST: Connection to twitter API
def ConnectAPI():
	api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET,\
			  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	return api

# PRE: N/A
# POST: Cute image link from cutestpaws.com 
def GetImage():
	# Get random animal to search for
	animals = ['kittens','pugs','cats','gerbils','bunnies','chipmunks','dogs','otters']
	animal = random.choice(animals)

	print('Gonna get a picture of {0}'.format(animal))
	# Get preview page for random animal
	PreHTML = requests.get('http://www.cutestpaw.com/?s={0}'.format(animal))
	PreHTML.raise_for_status()

	PreObject = bs4.BeautifulSoup(PreHTML.text, 'html.parser')

	if PreObject:
		print('Got preview page OK')

	# Get random picture from preview page
	photos = PreObject.select('#photos a')
	choice = random.choice(photos)

	if choice:
		print('Got choice of picture OK')

	# Get picture page
	PicHTML = requests.get(choice['href'])
	PicHTML.raise_for_status()

	PicObject = bs4.BeautifulSoup(PicHTML.text, 'html.parser')

	if PicObject:
		print('Got picture page OK')

	# Parse picture page for image
	img = PicObject.select('#single-cute-wrap img')
	link =  img[0]['src']

	if link:
		print('Got image link OK')
	return link

# Main Driver
def main():
	conx = ConnectAPI()
	
	if conx:
		print('Connected to Twitter OK')
	
	while True:
		mentions = conx.GetMentions()
		
		if mentions:
			print('Got {0} mentions'.format(len(mentions)))
			for mention in mentions:
				user = mention.user.screen_name

				if not mention.favorited:
					text = 'Hey @{0}, hope this brightens your day!'.format(user)
					img = GetImage()

					status = conx.PostUpdate(text,img)

					if status:
						print('Tweeted at {0} OK'.format(user))
					
					conx.CreateFavorite(status=mention)

				else:
					print('Already tweeted @{0}'.format(user))

		else:
			print('Got no mentions')

		print('Going to sleep..')
		time.sleep(60)
		print('Waking up!')

if __name__ == '__main__':
	main()
