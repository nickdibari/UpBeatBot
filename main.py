#! /usr/bin/python

# UpBeatBot
# Nicholas DiBari
# Twitter bot to tweet uplifting things

import bs4
import random
import requests
import twitter

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# PRE: N/A
# POST: Connection to twitter API
def ConnectAPI():
	# DELETE BEFORE PUSHING
	api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET,\
			  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	return api

# PRE: N/A
# POST: Cute image link from cutestpaws.com 
def GetImage():
	# Get random animal to search for
	animals = ['kittens','pugs','cats','gerbils','bunnies','chipmunks','dogs']
	animal = random.choice(animals)

	# Get preview page for random animal
	PreHTML = requests.get('http://www.cutestpaw.com/?s={0}'.format(animal))
	PreHTML.raise_for_status()

	PreObject = bs4.BeautifulSoup(PreHTML.text, 'html.parser')

	# Get random picture from preview page
	photos = PreObject.select('#photos a')
	choice = random.choice(photos)

	# Get picture page
	PicHTML = requests.get(choice['href'])
	PicHTML.raise_for_status()

	PicObject = bs4.BeautifulSoup(PicHTML.text, 'html.parser')

	# Parse picture page for image
	img = PicObject.select('#single-cute-wrap img')
	link =  img[0]['src']

	return link

# Main Driver
def main():
	conx = ConnectAPI()
	
	if conx:
		print('Connected to Twitter OK')
	
	mentions = conx.GetMentions()
	
	if mentions:
		print('Got {0} mentions'.format(len(mentions)))

	else:
		print('Got no mentions')
	
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

if __name__ == '__main__':
	main()
