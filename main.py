#! /usr/bin/env python

# UpBeatBot
# Nicholas DiBari
# Twitter bot to tweet uplifting things

import bs4
import twitter

from datetime import datetime as dt
import logging
import random
import requests
import string
import time as t

from twitter_auth import CONSUMER_KEY, CONSUMER_SECRET,\
                            ACCESS_TOKEN, ACCESS_TOKEN_SECRET


# PRE: N/A
# POST: Connection to twitter API

def ConnectAPI():
    api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET,
                      ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return api


# PRE: User tweet to parse
# POST: Animal to search for. Match from our list if found; else random animal
def get_animal(tweet):
    animals = [
        'kittens', 'kitten', 'pugs', 'pug', 'cats', 'cat', 'gerbils',
        'gerbil', 'bunnies', 'bunny', 'chipmunks', 'chipmunk', 'dogs',
        'dog', 'otters', 'otter', 'chinchillas', 'chinchilla', 'red pandas',
        'red panda', 'squirrel', 'squirrels'
    ]
    animal = None

    # Remove punctuation marks from tweet
    tweet = tweet.translate(None, string.punctuation)

    for word in tweet.split(' '):
        if word in animals:
            animal = word
            break

    if animal is None:
        animal = random.choice(animals)

    return animal


# PRE: Animal to search for on cutestpaws.com
# POST: Cute image link to tweet at user

def GetImage(animal):
    logging.info(' Gonna get a picture of {0}'.format(animal))

    # Get preview page for animal
    PreHTML = requests.get('http://www.cutestpaw.com/?s={0}'.format(animal))
    PreHTML.raise_for_status()

    PreObject = bs4.BeautifulSoup(PreHTML.text, 'html.parser')

    logging.info(' Got preview page OK')

    # Get random picture from preview page
    photos = PreObject.select('#photos a')
    choice = random.choice(photos)

    logging.info(' Got choice of picture OK')

    # Get picture page
    PicHTML = requests.get(choice['href'])
    PicHTML.raise_for_status()

    PicObject = bs4.BeautifulSoup(PicHTML.text, 'html.parser')

    logging.info(' Got picture page OK')

    # Parse picture page for image
    img = PicObject.select('#single-cute-wrap img')
    link = img[0]['src']

    logging.info(' Got image link OK')

    return link


# Main Driver

def main():
    logging.basicConfig(filename='dev.log', level=logging.INFO)
    tweet_text = 'Hey @{0}, hope this brightens your day!'

    i = 0
    while True:
        time = dt.now().strftime('%b %d, %Y @ %H:%M:%S')
        pass_info = ' --Pass: {0} | {1}--'.format(i, time)
        logging.info(pass_info)

        try:
            conx = ConnectAPI()
            logging.info(' Connected to API OK')
            mentions = conx.GetMentions()

            if mentions:
                logging.info(' Got {0} mentions'.format(len(mentions)))
                for mention in mentions:
                    user = mention.user.screen_name

                    if not mention.favorited:
                        logging.info(' Gonna tweet @{0}'.format(user))

                        text = tweet_text.format(user)
                        animal = get_animal(tweet)
                        img = GetImage(animal)

                        conx.PostUpdate(text, img)
                        logging.info(' Tweeted @{0} OK'.format(user))

                        conx.CreateFavorite(status=mention)

                    else:
                        logging.info(' Already tweeted @{0}'.format(user))

            else:
                logging.info(' Got no mentions')

        except Exception as e:
            print('Caught some exception at {}').format(pass_info)
            print('Check logs for more details')

            error_type = type(e[0])
            url = e[0].url

            logging.warning(' ERROR: Caught exception {}'.format(error_type))
            logging.warning(' Could not reach url: {}'.format(url))
            logging.exception(' Full traceback:')

        logging.info(' Going to sleep..')
        t.sleep(300)
        logging.info(' Waking up!')
        logging.info(' -----------------')
        i += 1  # increment pass number variable


if __name__ == '__main__':
    main()
