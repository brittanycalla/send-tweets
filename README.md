# Tweeting with Copilot

![A tweet from user @brittanycalla that says, "I wrote this tweet with Copilot - thank you @blackgirlbytes!"](https://i.ibb.co/MR4Nq3b/copilot-tweet.webp)

This is a simple program for sending tweets using the Twitter API. It was made using GitHub's Copilot!

![A screen recording showing a user typing comments into VSCode and GitHub Copilot making suggestions](https://i.ibb.co/d47VWfD/copilot-tweet-screen-demo.webp)

After attending [Level Up with GitHub Copilot](https://learning.oreilly.com/live-events/level-up-with-github-copilot/0636920090759/0636920090758) led by Rizel Scarlett, I decided to use Copilot to create a simple program to send tweets from the command line.

## How It's Made:

**Tech used:** Python, [Twitter API](https://developer.twitter.com/en/docs/twitter-api), [GitHub Copilot](https://github.com/features/copilot)

## Setup
**Twitter API**: If you've never used the Twitter API, you'll need to sign up for a Basic (free) [Developer Account](https://developer.twitter.com/en/portal/products/free). 
After that, go into your app's settings (a default project and app are created for you when you signup).

![A screenshot showing where to change Twitter API app settings](https://i.ibb.co/yY6tTx0/Screen-Shot-2023-04-04-at-3-43-49-PM.png)

We need to make some changes to our app's permissions. Click **Edit** under User authentication settings.
![A screenshot showing where to change Twitter API app user authentication settings](https://i.ibb.co/9qgbPJG/Screen-Shot-2023-04-04-at-3-44-04-PM.png)

From here, you'll want to make sure your app has read *and* write permissions.
![A screenshot showing where to change Twitter API app read and write permissions](https://i.ibb.co/DrN1Skm/Screen-Shot-2023-04-04-at-3-44-17-PM.png)

If you have any trouble, I found this writeup very helpful: [How to get started with the Twitter API in 2023](https://medium.com/@yassinetahri/how-to-get-started-with-the-twitter-api-in-2022-34b8f1d0d73a#:~:text=Click%20on%20the%20'Create%20a,content%20and%20status%20code%20201.)

Now we have the permissions necessary to send tweets! 
Grab your Consumer Key and Secret and generate an Access Token and Secret by going to your app's keys and tokens tab.
![A screenshot showing where to go to access your Twitter app's keys and tokens](https://i.ibb.co/VWD5Z7L/Screen-Shot-2023-04-04-at-4-00-37-PM.png)

You'll need to add your Twitter API Consumer keys and Access Tokens to the [config.py](https://github.com/brittanycalla/send-tweets/blob/main/config.py) file.

## Let's Tweet!
In the [sendTweet.py](https://github.com/brittanycalla/send-tweets/blob/main/sendTweet.py) file, swap out the text in the `tweet` variable with your desired message.
```
# create a variable with the text to tweet
tweet = "Hey GitHub!"
```

In your terminal run
```
python3 sendTweet.py
```



***Happy tweeting!***
