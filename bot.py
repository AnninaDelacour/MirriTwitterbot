import random
import tweepy
import time


consumer_key = '########'
consumer_secret = '#######'

key = '######'
secret = '######'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

file_name = 'last_seen.txt'

line = random.choice(open('quotes.txt').readlines())


def retrieve_id(file_name):
    file_read = open(file_name, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_id(id, file_name):
    file_write = open(file_name, 'w')
    file_write.write(str(id))
    file_write.close()
    return

def reply():
    last_id = retrieve_id(file_name)
    mentions = api.mentions_timeline(last_id, tweet_mode="extended")
    for mention in reversed(mentions):
        if '#mirribot' in mention.full_text:
            last_id = mention.id
            store_id(last_id, file_name)
            api.update_status('@' + mention.user.screen_name + line, mention.id)
            api.create_favorite(mention.id)
            api.retweet(mention.id)


while True:
    reply()
    time.sleep(2)