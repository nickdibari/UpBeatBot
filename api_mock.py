import random


class Dummy(object):
    """
    Dummy data object to hold arbitrary data. Good for mocking out various
    classes and data structures used in program execution.
    """
    def __init__(self):
        pass


class TwitterAPIMock(object):
    """
    Class that mimics the endpoints used in the program. Doesn't actually call
    the endpoints but instead returns fixture data similar to that of the
    actual Twitter API
    """
    def GetMentions(self, mentions=5):
        """
        Return data on user mentions
        return: List of Dummy objects that mimic the objects used in the
        Twitter API
        """
        mentions_list = []

        for i in range(mentions):
            mention = Dummy()
            mention.user = Dummy()

            mention.user.screen_name = 'Dummy'
            mention.tweet = 'Hey @UpBeatBot!'
            mention.favorited = True

            # Randomly determine to tweet at user
            # Also specify an animal to test that feature
            if random.randint(0, 10) % 2 == 0:
                mention.favorited = False
                mention.tweet += ' Send me a a picture of a {animal}'.format(
                    animal=random.choice(
                        ['dog', 'bunny', 'kitten', 'pug', 'squirrel']
                    )
                )

            mentions_list.append(mention)

        return mentions_list

    def PostUpdate(self, text, img):
        """
        Sends tweet to be posted. Doesn't actually return anything, so can
        be a simple `pass` method.
        """
        pass

    def CreateFavorite(self, status):
        """
        Favorites a specified tweet. Like with PostUpdate doesn't return
        anything in the real version so can be easily mocked
        """
        pass
