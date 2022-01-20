"""
Created on Thursday Jan 20 11:17:00 2022
@author: rishells
"""

from keys_twitter import api_key as consumer_key, api_secret_key as consumer_secret, access_token, access_token_secret
from curses import raw
from tweepy import OAuthHandler, Stream, StreamListener

import json

def extract_tweet_data(data):
    raw_json = json.loads(data) #
    id_str = raw_json['id_str']
    language = raw_json['lang']
    timestamp = raw_json['timestamp_ms']
    text = raw_json['text']
    user = raw_json['user']['screen_name']
    user_followers = raw_json['user']['followers_count']
    user_friends = raw_json['user']['friends_count']
    user_statues = raw_json['user']['statuses_count']
    user_creation = raw_json['user']['created_at']
    return [id_str, language, timestamp,text,user,user_followers,user_friends,
            user_statues,user_creation]

class StdOutListener(StreamListener):
    """ A Listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        list_data = extract_tweet_data(data)
        print('Usuario: {}, Mensaje: {}'.format(list_data[4], list_data[3]))

        # FUNCION PARA INSERTAR LOS DATOS EN BASE SQL
        test_list_origin.append(data)
        test_list.append(list_data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    # LISTA PARA VER COMO ESTRUCTURA DE DATOS
    test_list_origin = []
    test_list = []
    listener_ = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)


    
    stream = Stream(auth, listener_)
    stream.filter(track=['btc'])

    test = test_list_origin[0]
    raw_json = json.loads(test)

    f = open("raw_json.txt", "a")
    f.write(raw_json)
    f.close()
    