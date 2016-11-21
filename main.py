#! /usr/bin/python

# UpBeatBot
# Nicholas DiBari
# Twitter bot to tweet uplifting things

import bs4
import twitter

from datetime import datetime as dt
import logging
import random
import requests
import time as t

from twitter_auth import CONSUMER_KEY, CONSUMER_SECRET,\
                            ACCESS_TOKEN, ACCESS_TOKEN_SECRET


# PRE: N/A
# POST: Connection to twitter API

def ConnectAPI():
    api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET,
                      ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return api


# PRE: N/A
# POST: Cute image link from cutestpaws.com

def GetImage():
    # Get random animal to search for
    animals = ['kittens', 'pugs', 'cats', 'gerbils', 'bunnies', 'chipmunks',
               'dogs', 'otters', 'chinchillas', 'red pandas']
    animal = random.choice(animals)

    logging.info(' Gonna get a picture of {0}'.format(animal))
    # Get preview page for random animal
    PreHTML = requests.get('http://www.cutestpaw.com/?s={0}'.format(animal))
    PreHTML.raise_for_status()

    PreObject = bs4.BeautifulSoup(PreHTML.text, 'html.parser')

    if PreObject:
        logging.info(' Got preview page OK')

    # Get random picture from preview page
    photos = PreObject.select('#photos a')
    choice = random.choice(photos)

    if choice:
        logging.info(' Got choice of picture OK')

    # Get picture page
    PicHTML = requests.get(choice['href'])
    PicHTML.raise_for_status()

    PicObject = bs4.BeautifulSoup(PicHTML.text, 'html.parser')

    if PicObject:
        logging.info(' Got picture page OK')

    # Parse picture page for image
    img = PicObject.select('#single-cute-wrap img')
    link = img[0]['src']

    if link:
        logging.info(' Got image link OK')

    return link


# Main Driver

def main():
    logging.basicConfig(filename='dev.log', level=logging.INFO)

    i = 0
    while True:
        time = dt.now().strftime('%b %d, %Y @ %H:%M:%S')
        logging.info(' --Pass: {0} | {1}--'.format(i, time))
        conx = ConnectAPI()

        if conx:
            logging.info(' Connected to API OK')

        mentions = conx.GetMentions()

        if mentions:
            logging.info(' Got {0} mentions'.format(len(mentions)))
            for mention in mentions:
                user = mention.user.screen_name

                if not mention.favorited:
                    logging.info(' Gonna tweet @{0}'.format(user))

                    text = 'Hey @{0}, hope this brightens your day!'\
                           .format(user)
                    img = GetImage()

                    status = conx.PostUpdate(text, img)

                    if status:
                        logging.info(' Tweeted @{0} OK'.format(user))

                    conx.CreateFavorite(status=mention)

                else:
                    logging.info(' Already tweeted @{0}'.format(user))

        else:
            logging.info(' Got no mentions')

        logging.info(' Going to sleep..')
        t.sleep(300)
        logging.info(' Waking up!')
        logging.info(' -----------------')
        i += 1  # increment pass number variable


if __name__ == '__main__':
    main()
