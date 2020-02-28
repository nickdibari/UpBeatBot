# UpBeatBot
Twitter bot to tweet uplifting images at twitter users

## Usage
Simply tweet a mention at UpBeatBot (@UpBeatBot) on Twitter to receive a cute picture tweeted at you

## Running UpBeatBot
To run UpBeatBot on your own, download the source code and create a .env file that contains your twitter bot's authentication keys. You can copy the .example_env file to .env and replace with your relevant keys
- Follow the guide on https://dev.twitter.com/oauth/overview/application-owner-access-tokens to register your app and get credentials

Next, create a Python virtual environment running python3. Assuming you have the `virtualenv` package installed, you can run the following command in this directory to get it set up:

`virtualenv -p $(which python3) venv`

Activate the virtual environment by entering `source venv/bin/activate` from the project directory

Finally, install the requirements by entering `pip install -r requirements.txt` from the project root. This will install the needed dependencies in the virtual environment for use by the program

Runing `./main.py` will start the TwitterBot, it will log information about program execution to a log file (dev.log)
in the directory UpBeatBot is stored in

## Running Unit Tests
To run the unit tests for this project, enter `python -m unittest discover -v` from the project root. You'll see the output
of every test method, and if any fail an explanation as to why they failed.


## Packing Application
To build UpBeatBot for publishing to PyPi, you'll need to build and upload the `upbeatbot` package

1. Build the package

`python setup.py bdist bdist_wheel`

2. Upload to PyPi

`python -m twine upload dist/*`
