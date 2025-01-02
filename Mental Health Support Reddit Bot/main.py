import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "mental_health_bot v.2")
    return r

def check_for_context(submission):
    #check for distress-related phrases
    distress_phrases = [
        "I feel hopeless", "I can't cope", "I need help", "I'm struggling", 
        "I feel lost", "I can't go on", "I'm thinking of ending it", "I feel like giving up",
        "I'm overwhelmed", "I can't breathe", "I don't know what to do", "I am lost", 
        "I'm feeling numb", "I feel trapped", "I'm in pain", "I'm having a hard time", 
        "I can't focus", "I can't stop crying", "I'm anxious", "I'm depressed", "I'm scared"
    ]
    for phrase in distress_phrases:
        if phrase in submission.title.lower() or phrase in submission.selftext.lower():
            return True
    return False

def run_bot(r):
    # Monitor the 'mentalhealth' subreddit
    for submission in r.subreddit('mentalhealth').new(limit=25):
        if check_for_context(submission):
            # Respond to distress related to mental health issues
            if 'gambling addiction' in submission.title.lower() or 'gambling addiction' in submission.selftext.lower():
                print("Gambling addiction distress found")
                submission.reply(
                    "I can sense you're struggling with gambling addiction. Please, reach out to a professional for support: \n\n"
                    "Canada: National Gambling Helpline - 1-800-463-1554\n"
                    "USA: National Problem Gambling Helpline - 1-800-522-4700\n"
                    "UK: National Gambling Helpline - 0808 8020 133\n\n"
                    "Please talk to someone who can help you through this. You're not alone."
                )
            elif 'depression' in submission.title.lower() or 'depression' in submission.selftext.lower():
                print("Depression distress found")
                submission.reply(
                    "I'm really sorry you're feeling this way. Depression can be overwhelming, but there is help available. Please reach out to the following helplines: \n\n"
                    "Canada: Kids Help Phone - 1-800-668-6868 (Text 686868)\n"
                    "USA: National Suicide Prevention Lifeline - 1-800-273-8255\n"
                    "UK: Samaritans - 116 123\n\n"
                    "You matter, and help is just a phone call away. Please reach out to someone who cares about your well-being."
                )
            elif 'suicide' in submission.title.lower() or 'suicide' in submission.selftext.lower():
                print("Suicide distress found")
                submission.reply(
                    "I'm really sorry you're feeling this way, but please know that you can get help. It's important to talk to someone right away: \n\n"
                    "Canada: Crisis Services Canada - 1-833-456-4566\n"
                    "USA: National Suicide Prevention Lifeline - 1-800-273-8255\n"
                    "UK: Samaritans - 116 123\n\n"
                    "You are not alone. Please reach out to someone now. There is hope."
                )
            elif 'anxiety' in submission.title.lower() or 'anxiety' in submission.selftext.lower():
                print("Anxiety distress found")
                submission.reply(
                    "Anxiety can be overwhelming, but you don’t have to face it alone. Please consider reaching out to the following helplines: \n\n"
                    "Canada: Anxiety Disorders Association of Canada - 1-866-781-2607\n"
                    "USA: National Helpline for Mental Health - 1-800-662-HELP\n"
                    "UK: Anxiety UK Helpline - 03444 775 774\n\n"
                    "It’s okay to reach out. You're stronger than you think, and there’s support available."
                )
            else:
                # Default response for any distress signals that aren't categorized
                submission.reply(
                    "It sounds like you're going through something really difficult right now, but please know that help is available. Reach out to someone who can support you: \n\n"
                    "Canada: Kids Help Phone - 1-800-668-6868\n"
                    "USA: National Suicide Prevention Lifeline - 1-800-273-8255\n"
                    "UK: Samaritans - 116 123\n\n"
                    "You're not alone. There are people who care and want to help."
                )

r = bot_login()
run_bot(r)