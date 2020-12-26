import tweepy
import datetime

credentials = open("credentials.txt", 'r').read().split('\n')

consumer_key = credentials[0]
consumer_secret = credentials[1]
access_token = credentials[2]
access_token_secret = credentials[3]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def publictweet():
    print('Escriba el tweet que será publicado')
    print('*Cuando termine solo presione enter')
    string = str(input())
    api.update_status(string)
    print('Mensaje publicado con exito',string)

publictweet()
