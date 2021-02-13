import json
import twint
import tweepy
import pycountry
import datetime
import time
from geopy.geocoders import Bing

events = ["San Francisco", "New York", "Cowes"]
data_files = ["San_Francisco.json", "New_York.json", "Cowes.json"]

invalid_locations = ["Global", ""]

locator = Bing("Ah0nnAJPsuz_GDQuwBEQ0xplFqJy7MsoCwLGDmTyZwA_RcTKsQKPY0X0MFf3rh5j")


with open("key.txt", "r") as f:
    keys = f.read().split("\n")

# api = twitter.Api(consumer_key=keys[0], consumer_secret=keys[1], access_token_key=keys[2], access_token_secret=keys[3])

auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])

api = tweepy.API(auth)

for i, event in enumerate(events):
    nums = {}
    with open(data_files[i], "r", encoding="utf8") as f:
        data = f.read().split("\n")
    
    for i, t in enumerate(data):
        print(i)
        try:
            tweet = json.loads(t)
        except:
            continue
        username = tweet["username"]
        # u = twint.Config()
        # u.Username = username
        # u.Store_object = True
        # try:
        #     twint.run.Lookup(u)
        # except:
        #     print("exception caught")
        #     continue
        # user = twint.output.users_list[0]

        try:
            user = api.get_user(username)
        except:
            print("SLEEPING")
            time.sleep(900)
            try:
                user = api.get_user(username)
            except:
                continue

        if user.location in invalid_locations:
            continue
        
        try:
            loc = locator.geocode(user.location, timeout=10)
        except:
            continue

        if not loc:
            continue

        country = " ".join(loc.address.split(",")[-1].split())

        code = pycountry.countries.get(name=country)

        if code:
            if code.alpha_3 in nums.keys():
                nums[code.alpha_3] += 1
            else:
                nums[code.alpha_3] = 1
        else:
            continue
        
    with open("{}.csv".format(event), "w") as f:
        f.write("\n".join(["{},{}".format(key, nums[key]) for key in nums.keys()]))