import tweepy
import random
import keys
from mk1 import actors_list, directors_list, franchise, actortwt, franchisetwt, directortwt, character, charactertwt

def api ():
    auth = tweepy.OAuthHandler (keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)

def tweet (api: tweepy.API, message: str, image_path = None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status (message)
    
    print ('success')


#api = tweepy.API(auth, wait_on_rate_limit=True,
    #wait_on_rate_limit_notify=True)

randomcase = random.randint(1,10)

#api.update_status

match randomcase:
    case 1: 
        message = "A new " + str (franchise[franchisetwt]) + " movie in the works with " + str (actors_list[actortwt]) + " set to star, " + str (directors_list[directortwt]) + " is a possible director. "
    case 2: 
        message = "It looks like " + str (directors_list[directortwt]) + " wants to do a " + str (franchise[franchisetwt]) + " reboot, with " + str (actors_list[actortwt]) + " as the lead. "
    case 3:
        message = "Our sources say that " + str (actors_list[actortwt]) + " has been casted as " + str(character[charactertwt]) + " in a new " + str (franchise[franchisetwt]) + " with " + str (directors_list[directortwt]) + " set to direct."
    case 4:
        message = "The " + str(franchise[franchisetwt]) + " cinematic universe has been canceled."
    case 5:
        message = "A new " + str (franchise[franchisetwt]) + " series adaptation is in the works from " + str(directors_list[directortwt]) + "."
    case 6:
        message = str(actors_list[actortwt]) + " hinted at the possibility of being casted in a " + str(franchise[franchisetwt]) + " series."
    case 7: 
        message = str(actors_list[actortwt]) + " has filmed a cameo as " + str(character[charactertwt]) + " for the new " + str(franchise[franchisetwt]) + " movie."
    case 8:
        message = "The " + str(franchise[franchisetwt]) + " remake is no longer moving forward."
    case 9:
        message = str(actors_list[actortwt]) + " will voice " + str(character[charactertwt]) + " in the next " + str(franchise[franchisetwt]) + " universe installment."
    case 10:
        message = "The " + str(franchise[franchisetwt]) + " series adaptation will premier next year on Disney+."


if __name__ == '__main__':
    api = api()
    tweet (api, message)
 