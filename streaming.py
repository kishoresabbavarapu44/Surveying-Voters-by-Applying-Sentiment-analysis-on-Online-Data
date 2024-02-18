import tweepy
import json
import csv
import urllib



#run this code after provinding twitter consumer and access keys below
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

accountvar = "YSRCParty"  #Search query goes here
outputfilecsv = "data/"+accountvar+"_stream.csv"
fc = csv.writer(open(outputfilecsv, 'w'))
#fc.writerow(["created_at","screen_name","tweet_text","time_zone"])

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        
        decoded = json.loads(data)
        try:
            print (decoded['entities']['media'][0]['media_url'])
            link = decoded['entities']['media'][0]['media_url']
            filename = link.split('/')[-1]
            urllib.urlretrieve(decoded['entities']['media'][0]['media_url'],filename)
             
            for media in decoded['extended_entities']['media'][0]['video_info']['variants']:
                if 832000 in media.values():
                    link = media['url']
                    filename = link.split('/')[-1]
                    urllib.urlretrieve(media['url'],filename)
                       
                        
        except (NameError, KeyError,AttributeError):
                        #we dont want to have any entries without the media_url so lets do nothing
             pass
        
        print ('%s @%s: %s %s\n' % (decoded['created_at'],decoded['user']['screen_name'],decoded['text'].encode('ascii', 'ignore'),decoded['user']['time_zone']))
        fc.writerow([decoded['created_at'],decoded['user']['screen_name'],decoded['text'].encode('ascii', 'ignore'),decoded['user']['time_zone']])     

         #got media_url - means add it to the output
        
        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        
        #print ''
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    print ("Showing all new tweets for %s"%accountvar)

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=[accountvar])
