import tweepy
import json
import hidden
import sys


def initialize():
    oauth = hidden.oauth()

    auth = tweepy.OAuthHandler(oauth['consumer_key'], oauth['consumer_secret'])
    auth.set_access_token(oauth['token_key'], oauth['token_secret'])
    return tweepy.API(auth, parser=tweepy.parsers.JSONParser())


def getValueFromJSON(key, dct):
    return dct[key]


def read_print_key(user):
    # show hint for user
    print("user JSON has the next keys:")
    for i in user:
        print("---", i)

    while True:
        # read key
        key = input("Please, enter the key of json that you want to read: ")

        if key not in user:
            print('Sorry, but there is no key "', key, '" in the json')
            continue

        print("\nThere is the value of chosen key: ")
        print(getValueFromJSON(key, user))

        # ask user whether continue discovering JSON
        if type(getValueFromJSON(key, user)) == dict:
            check = input("\nIf you want to go deeper into the JSON, press 1: ")
            if check == '1':
                read_print_key(getValueFromJSON(key, user))
        break


if __name__ == '__main__':
    api = initialize()

    # get user info
    while True:
        nickname = input("Enter the nickname of user who you want to get information about: ")

        if not nickname:
            sys.exit(0)
        try:
            user = api.get_user(screen_name=nickname)
            break
        except tweepy.error.TweepError:
            print('Sorry, but there is no user with nickname "', nickname, '"')

    read_print_key(user)


