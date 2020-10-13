import os
import random
import schedule
import time
import tweepy

from dotenv import load_dotenv
load_dotenv()
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_secret = os.getenv("access_secret")

directory = r"C:\\Users\\Gwendolyn\Desktop\Bots (Twitter)\\Random Profile Image\\images"


def twitter():                  
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    return api

def bot(): 
    try: 
        image = random.choice(os.listdir(f"{directory}"))
        print(f"{image} has been selected.")

        twitter().update_profile_image(filename = f"{directory}\\{image}")
        print(f"Now using {image} as the profile picutre!")

        os.remove(f"{directory}\\{image}")        
        print(f"Task completed.\n-----")    
    except tweepy.TweepError as e: 
        print(f"Exception raised!\nCode: {e.api_code}\nReason: {e.reason}")
    
        if e.reason == "File is too big, must be less than 700kb.":
            print(f"{image} is too large to use. Deleting!")
            os.remove(f"{directory}\\{image}")
            print(f"There are {len(os.listdir(directory))} images left in {directory}")
    finally: 
        pass

schedule.every().day.at("00:00").do(bot)

while len(os.listdir(f"{directory}")) != 0:
    schedule.run_pending()
    time.sleep(1)
else:
    print(f"{directory} is empty.")