import logging
import sys
from datetime import datetime as dt
from time import sleep

import twitter

import settings
from libs.api_mock import TwitterAPIMock
from libs.upbeatbot import UpBeatBot

log_format = '%(levelname)s: %(asctime)s %(message)s'
log_date_format = '%Y-%m-%d %H:%M:%S'

logging.basicConfig(
    filename=settings.LOG_FILE,
    level=logging.INFO,
    format=log_format,
    datefmt=log_date_format,
)


# Debug config
DEBUG = '--debug' in sys.argv or settings.DEBUG


def connect_api():
    return twitter.Api(
        settings.CONSUMER_KEY,
        settings.CONSUMER_SECRET,
        settings.ACCESS_TOKEN,
        settings.ACCESS_TOKEN_SECRET
    )


def main():
    tweet_text = 'Hey @{0}, hope this brightens your day!'
    pass_number = 0
    upbeat_bot = UpBeatBot()

    while True:
        time = dt.now().strftime('%b %d, %Y @ %H:%M:%S')
        pass_info = '--Pass: {} | {}--'.format(pass_number, time)
        logging.info(pass_info)

        try:
            if DEBUG:
                conx = TwitterAPIMock()
            else:
                conx = connect_api()

            mentions = conx.GetMentions()

            if mentions:
                logging.info('Got {} mentions'.format(len(mentions)))

                for mention in mentions:
                    user = mention.user.screen_name

                    if not mention.favorited:
                        logging.info('Gonna tweet @{}'.format(user))
                        logging.info('User tweet: {}'.format(mention.text))

                        text = tweet_text.format(user)
                        img = upbeat_bot.get_cute_animal_picture(mention.text)
                        logging.info('Using image: {}'.format(img))

                        # Don't actually tweet the test account
                        if user != 'upbeatbottest':
                            conx.PostUpdate(text, img)
                            logging.info('Tweeted @{} OK'.format(user))

                        conx.CreateFavorite(status=mention)

                    else:
                        logging.info('Already tweeted @{}'.format(user))

            else:
                logging.info('Got no mentions')

        except twitter.error.TwitterError as conn_error:
            logging.exception(
                'Caught exception {type} trying to connect to API at pass: {pass_number} \n'
                'Full traceback:'.format(type=conn_error.__class__.__name__, pass_number=pass_number)
            )

        except Exception as exc:
            logging.exception(
                'Unhandled exception {exc} at pass: {pass_number} \n'
                'Full traceback:'.format(exc=exc.__class__.__name__, pass_number=pass_number)
            )

        logging.info('Going to sleep for {}s..'.format(settings.SLEEP_TIMEOUT))
        sleep(settings.SLEEP_TIMEOUT)
        logging.info('Waking up!')
        logging.info('-----------------')
        pass_number += 1


if __name__ == '__main__':
    main()
