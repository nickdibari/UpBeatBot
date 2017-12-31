# UpBeatBot
Twitter bot to tweet uplifting images at twitter users

## Usage
Simply tweet a mention at UpBeatBot (@UpBeatBot) on Twitter to receive a cute picture tweeted at you

## Running UpBeatBot
To run UpBeatBot on your own, download the source code and create a file name twitter_auth.py that contains your twitter bot's authentication keys

Follow the guide on https://dev.twitter.com/oauth/overview/application-owner-access-tokens to register your app and get credentials

Runing `./main.py` will start the TwitterBot, it will log information about program execution to a log file (dev.log) in the directory UpBeatBot is stored in

## Running Unit Tests
To run the unit tests for this project, enter `python -m unittest -v test` from the project root. You'll see the output of every test method, and if any fail an explanation as to why they failed
