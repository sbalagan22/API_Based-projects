# Mental Health Support Reddit Bot

## Overview

The **Mental Health Support Reddit Bot** is a Python-based bot that monitors submissions on the **mentalhealth** subreddit for distress-related phrases. Upon detecting distress signals related to various mental health topics such as gambling addiction, depression, anxiety, and suicidal thoughts, the bot provides helpful responses with relevant helplines for Canada, USA, and the UK. The bot aims to offer immediate, supportive messages to individuals who may be struggling, encouraging them to seek professional help and reminding them that they are not alone.

This project focuses on using technology to offer emotional support to people experiencing mental health challenges. It addresses the increasing need for mental health resources in an online environment and strives to create a more compassionate and informed online community.

## Features

- **Real-time monitoring of Reddit**: The bot monitors new submissions in the **mentalhealth** subreddit.
- **Context-based response**: The bot identifies distress-related phrases and responds with a customized message for specific mental health topics.
- **Resourceful and compassionate**: Offers helpful resources such as hotlines for various mental health issues like gambling addiction, depression, anxiety, and suicidal thoughts.
- **Multiple regions supported**: Provides hotlines for Canada, USA, and the UK.

## Why This Project is Impactful

Mental health struggles can often be isolating, and it can be difficult for people to find immediate help when they need it most. By leveraging the power of automated technology, this bot seeks to provide a first point of contact for those in distress and encourage them to reach out to trusted professionals.

- **Immediate response**: The bot responds instantly when distressing topics are detected, giving users quick access to resources.
- **Anonymity**: Since Reddit is an anonymous platform, people who may be hesitant to seek help in person can anonymously receive support.
- **Comprehensive coverage**: The bot offers a wide range of mental health issues, from addiction to emotional distress, ensuring it can help a variety of individuals.

This bot is a step toward reducing mental health stigma and making support resources more accessible. While it is not a substitute for professional help, it can provide users with the encouragement and resources they need to take the next step toward healing.

## How to Use

### Requirements

1. **Python 3.6+**: Make sure you have Python installed on your system.
2. **Praw**: The bot uses the `praw` library to interact with Reddit.
3. **Reddit Developer Account**: You need a Reddit account and a registered Reddit app to obtain the necessary API credentials.

### Setup Instructions

#### 1. Install Dependencies
Install the required libraries using `pip`. In your terminal, run:

```bash
pip install praw
```
2. Create config.py

In the same directory as the bot script, create a file named config.py that contains the necessary credentials for Reddit API access. You can obtain these credentials by registering an application in your Reddit account settings.

Here is an example of how config.py should look:

```
username = 'your_reddit_username'
password = 'your_reddit_password'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
```
3. Running the Bot

Once your config.py is in place, you can run the bot using the following command in the terminal:
```
python mental_health_bot.py
```
The bot will start monitoring new submissions in the mentalhealth subreddit. When it detects distress-related phrases, it will respond with appropriate support messages and resources.

### Customization

Feel free to customize the bot’s behavior:
	•	Modify the distress phrases: You can add or remove distress-related phrases in the check_for_context() function to tailor the bot to your needs.
	•	Extend the response: You can change the content of the responses, adding more helplines or modifying the text to better fit the audience.

### Important Notes
This bot is not a replacement for professional mental health services: While the bot provides valuable resources and compassionate responses, it is not intended 		to replace therapy or emergency services.

Use at your own risk: By running this bot, you are responsible for ensuring its ethical use. Monitor the bot’s activity to ensure it operates in a way that aligns with your values and respects the Reddit community guidelines
