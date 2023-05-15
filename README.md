# Run the project
- Create a virtual environment with `python3 -m venv venv` and pip install the requirements with `pip install -r requirements.txt`
- Create a .env and add a variable `BOT_TOKEN='token'` with the token of your bot
- Run the bot with `python3 bot.py` or run the .ipynb file

## Type !help when the bot is running to see all the commands
Here is a rundown of the major functionalities anyway:
## Bot functionalities

This bot has multiple functionalities:

1. It has an history of all the messages sent in the channel, and it can be searched by the user.
    - Implementation is done by a Stack and stored in a json file

2. The history has a built in wait list so that a data cannot be accessed by multiple users at the same time.
    - Implementation is done by a Queue

3. It has a discussion system that permits to find an answer on a specific topic. USAGE: `/ask <topic> <question>`
    - Implementation is done by a Tree and stored in a json file

4. There is a second implementation of logs that permits to store history of commands for each user. USAGE: `/log <user> <command>`
    - Implementation is done by a hashmap and stored in a json file

5. The bot data is stored in a json file so if the bot is restarted, the data is not lost.
    - 

6. The bot has a built in help command that explains all the functionalities of the bot. USAGE: `/commands`

# Table of content

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Discord bot that has multiple functionalities like history of commands, mini games and more..

## Project features
- History of commands (implemented with a stack)
- Discussion system (implemented with a tree)
- Logs of commands per user (implemented with a hashmap)
- Persistent data (implemented with json files)
- Help command
- Mini games
- Moderation commands

## Installation
Make sure you have **python** installed on your system
Run ```pip install -r requirements.txt``` to install all the dependencies
<br><br>
If you have any problems with the installation, you can open an issue in this repository.

## Usage
Run the .ipynb file

## Contributing
If you want to contribute to this project you can fork this repository and make a pull request with your changes.
Anyone is welcome to contribute to this project.

## License
This project is under the MIT license.