# Facebook FaceBot

Facebot is a Facebook bot with various functions for automation for posting.


# Login with a Facebook account

> **Note:** Chromedriver must be in path

> from Facebot_Extrabom import Facebook

> facebot = Facebook.Facebook()

> facebot.setLogin(login='[YOUR EMAIL FACEBOOK]' , senha='[YOUR PASSWORD]') 

## Posting

>groupID = ['1889352911359628'] # ID of the **group** you want to post
>facebot.setGrouopIds(groupID)
>Posts = ['Hello World'] # Message you will post
>facebot.start(posts=Posts)


## Stop bot

>facebot.stop()
