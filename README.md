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