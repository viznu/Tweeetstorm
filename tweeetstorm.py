import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
 
msg_array= [ #fill array up with messages 
]

  # Generate all these tokens by using Twitter's Application Developer platform
  cfg = { 
    "consumer_key"        : " ENTER ",
    "consumer_secret"     : " GENERATED ",
    "access_token"        : " VALUES ",
    "access_token_secret" : " HERE " 
    }

  api = get_api(cfg)

  for i in msg_array:
  	tweet = i
  	status = api.update_status(status=tweet) 

if __name__ == "__main__":
  main()
