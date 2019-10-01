# ROFI GTD

Dead simple python script for people who like Rofi, GTD and Trello. If so, please note that this a very minimalist project, yet it may be a good starting poin to any pythonista who desire to manipulate trello boards using Rofi.


# Configuration and requirements

You need python3, pipenv, rofi, a Trello account.
Go find your Trello API keys there https://trello.com/app-key and generate a token. Keep these secrets and edit your `settings.py` accordingly.
Use the trick described [here](https://customer.io/actions/trello/) to find the id of the lists you will use and edit your settings accordingly. 

- INBOX_LIST = Your Inbox List (where the stuff goes in)
- ACTION_LIST = Your Next Actions List (where actionnable stuff goes in)
- PROCESS_LIST = The Actions you will do today or you are doing right now
- NOTES_LIST = Your Inbox for ideas (I don't think it's in the GTD methodology but I personally like to have this alternative inbox for things I know right off the bat that won't be actionnable).

## Features

- Add stuff in your INBOX
- Add stuff in your Notes_LIST
- Show Next Actions and the select an action to either :
	- Show more (labels and description)
	- Add it in the PROCESS_LIST
	- Open it with your web browser


# Usage

```bash
git clone https://github.com/brumar/trellorofi.git
cd trellorofi
pipenv install -r requirements.txt
```
Note: On my machine it fails to install a dependency (the rofi-python fork). What I generally do is to activate the venv, then pip install the dependency manually.

Then edit your settings.py as explained above. Then :

```
pipenv run python trellorofi.py
```

If you use Rofi itself to launch your scripts (which you probably do), add this bash script to your script directory :
```
#!bin/bash
cd <path-to-trellorofi.py>
pipenv run python trellorofi.py
```

Using pipenv is my favorite trick to run a python script with its proper virtualenv activated.
If you don't use pipenv, activate your virtualenv as you usually do.

# A notes on dependencies

Rofi is called using the awesome [python-rofi](https://github.com/bcbnz/python-rofi). Yet I wanted some adjustements on the initial project, so the dependency used is a little fork I made.

# Missing Features

At the time of this Readme, the script is just 66 lines of code. If you know a little bit of python, You won't have any difficulty to change and add features. I am not sure what I would do with pull requests (if any). If you do a nice fork, please publicize it in the section below.

# Interesting forks

URL ; What's in there

# License

MIT
