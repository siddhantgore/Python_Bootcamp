
from nltk.util import tokenwrap
from textblob import TextBlob
import tweepy
import re
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
# data="Good boy"

# blob=TextBlob(data)

# print(blob.sentiment.polarity)
consumer_key="auvfFhsayOo8mnNZ3WatpXDEx"

consumer_secret="DyWBY0N97xflzhV757KRvs7oxplOU70A9v9wHLZnB0yns7PGVW"

key="1282486789274513409-Thz1WkEnDu6owSi99b45ur8rSyZw8P"

secret="RpM6c3CAErRczNJWtHiAVZFQ5xedqaGKDE8tusfLxs1H2"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api=tweepy.API(auth)

search_term=input("Enter the keyword:- ")
no_of_search_term=int(input("Enter No of records you want:- "))

tweets=tweepy.Cursor(api.search_tweets, q=search_term,lang="en").items(no_of_search_term)

twitter = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAM02XQEAAAAAO3bhydUcxkCu47fOUngtPCB2J%2BM%3DXNjxcP79b1jUYmYCWfHh8ffW0GpZGRp6iGTIjssvENSFrI65mM")

polarities=[]
tokenized_data=[]

for tweet in tweets:
    lower=tweet.text.lower()
    print("Tweet data:- "+str(lower))
    clean_data = re.sub(r"@\S+", "", lower)
    clean_data=re.sub(r"http\S+", "", clean_data)
    print("clean data:- "+str(clean_data))
    paolarity=(TextBlob(clean_data).sentiment.polarity)
    polarities.append(paolarity)
    print("Polarity:- "+str(paolarity))
    # tokenized_data = result1.apply(word_tokenize)      
    steamed_data=" ".join([stemmer.stem(word) for word in clean_data])
    # print("Steamed data is:- "+str(steamed_data))
    status = api.get_status(tweet.id)
    retweet_count = status.retweet_count

    print("Retweets:-"+str(retweet_count))
    print("User:- "+"".join(tweet.text.split(":")[0]).strip("RT @"))
    print("Tweeted at:- "+str(tweet.created_at))
    try:
        print("Followers:- "+str(twitter.get_user(username=("".join(tweet.text.split(":")[0]).strip("RT @")), user_fields=["public_metrics"]).data.public_metrics['followers_count']))
    except:
        pass
    print('\n')


result=((sum(polarities)*100)/no_of_search_term)
if result<0:
    print("Tweets contain Negetivity")
    print("Polarity Analysis is "+str(result))
else:
    print("Tweets contain Positivity")
    print("Polarity Analysis is "+str(result))
