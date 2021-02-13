import tweepy
import json
import string
import pycountry
import datetime
import GetOldTweets3 as got
from geopy.geocoders import Bing

with open("key.txt", "r") as f:
    keys = f.read().split("\n")

# api = twitter.Api(consumer_key=keys[0], consumer_secret=keys[1], access_token_key=keys[2], access_token_secret=keys[3])

auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])

api = tweepy.API(auth)

invalid_locations = ["Global", ""]
# dates = {"Sydney": ["201902010000", "201903020000"], "San Francisco": ["201904200000", "201905200000"], "New York": ["201906060000", "201907070000"], "Cowes": ["201907260000", "201908260000"]}
dates = {"Sydney": ["2019-02-01", "2019-03-02"], "San Francisco": ["2019-04-20", "2019-05-20"], "New York": ["2019-06-06", "2019-07-07"], "Cowes": ["2019-07-26", "2019-08-26"]}
data = {}

def check_tweets(tweets, nums, locator):
    for t in tweets:
        user = api.get_user(t.user)
        print(user)
        return
        if tweet.user.location in invalid_locations:
            continue

        loc = locator.geocode(tweet.user.location, timeout=10)

        if not loc:
            continue

        country = " ".join(loc.address.split(",")[-1].split())

        code = pycountry.countries.get(name=country)

        if code:
            if code.alpha_3 in nums.keys():
                nums[code.alpha_3] += 1
            else:
                nums[code.alpha_3] = 1
    # date_obj = datetime.datetime.strptime(tweets[-1].created_at, "%a %m %d %H:%M:%S %z %Y")
    return tweets[-1].created_at.strftime("%Y%m%d%H%M")

def get_tweets():
    locator = Bing("Ah0nnAJPsuz_GDQuwBEQ0xplFqJy7MsoCwLGDmTyZwA_RcTKsQKPY0X0MFf3rh5j")
    for event in dates.keys():
        nums = {}
        times = 1
        amount = 100

        criteria = got.manager.TweetCriteria().setSince(dates[event][0]).setUntil(dates[event][1]).setQuerySearch("sailgp")
        print(len(got.manager.TweetManager.getTweets(criteria)))
        break

        # tweets = api.search_full_archive("dev", "sailgp", fromDate=dates[event][0], toDate=dates[event][1], maxResults=amount)
        # check_tweets(tweets, nums, locator)
        # tweets = api.search_full_archive("dev", "sailgp", fromDate=dates[event][0], toDate=dates[event][1], maxResults=amount)
        # while len(tweets) == amount:
        #     times += 1
        #     final_date = check_tweets(tweets, nums, locator)
        #     tweets = api.search_full_archive("dev", "sailgp", fromDate=final_date, toDate=dates[event][1], maxResults=amount)
        #     print(times)
        # print(event)
        data[event] = nums

    with open("output.json", "w") as f:
        f.write(json.dumps(data))

if __name__ == "__main__":
    get_tweets()
