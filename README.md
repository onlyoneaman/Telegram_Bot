# Telegram_Bot
A introductory repository which helps you set up a bot in telegram which sends over messages to channels whenever program is runned

* **We will be making a program which sends over the Bitcoin price in INR to a channel via Bot.**

#### What is Bitcoin?

*  A software developer going by the name of Satoshi Nakamoto proposed bitcoin in 2008, as an electronic payment system based on mathematical proof. The idea was to produce a means of exchange, independent of any central authority, that could be transferred electronically in a secure, verifiable and immutable way.

* Since its launch in 2009, Bitcoin has been a controversial concept. Some people accept it as an anonymous currency, which protects their privacy and also provides a unified platform for all kinds of transactions online. Whereas there are others who shun it saying that it's the currency of the black market.

* But, the recent upshoot of the Bitcoin price has made everyone want to invest in it. There are stories about people who paid 25,000 Bitcoins for a pizza back in 2009-10 and are now regretting that decision. Whereas there are others who are running mining rigs and farms and making millions. But, it is not necessary that the Bitcoin price always stays high. Sometimes it rises and sometimes it falls so why not build a system that tells us when it rises and when it falls.

### What is Telegram?

Telegram is a messaging app similar to Whatsapp. You can send and receive messages along with files also. It is FREE to use. You can access the platform via your Android/iOS/Windows phone and also your PC or Mac.

![TELEGRAM_LOGO](/images/t_logo.png)

### Some Telegram terminologies -

#### What is a Telegram channel?

A channel is to Telegram what Groups are to Whatsapp. Channels are a tool for broadcasting your messages to large audiences. They can have an unlimited number of subscribers, they can be public with a permanent URL and each post in a channel has its own view counter.

#### What is a Bot?

Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages, commands and requests. 

We will be using Bots to send alerts on our channel.

#### Setup Telegram

Steps to sign-up for/sign-in to Telegram
1. Go to the Playstore or App Store on your phone and search for Telegram.
2. Download and Install the latest version of Telegram app.
3. Signup for a new account or sign in to Telegram by providing your mobile number.
4. Telegram will call you OR send you a SMS to verify your mobile number.
5. Get your account verified and approve any permissions if required.
6. You will be logged in to Telegram and will be shown a screen similar to the one below. (It's okay if it differs from the screenshot below)

![Tele Screenshot](/images/app_home.png)

7. You have successfully installed Telegram and setup your account. In the next lessons, we will be learning more about Channels and Bots.

### What is a Telegram channel?

A channel is to Telegram what Groups are to Whatsapp. Channels are a tool for broadcasting your messages to large audiences. They can have an unlimited number of subscribers, they can be public with a permanent URL and each post in a channel has its own view counter.

Steps to create a channel
* Go to the home screen of the Telegram app.
* Swipe from the left side to reveal the menu.
* Click on "New Channel".

![screenshot 1](/images/s1.png)

* It will ask you for a Name and Description for your channel. Give a suitable name and description. Adding photo is optional.

![screenshot 2](/images/s2.jpeg)

* In the next screen set the channel as Public.
* On the same screen, it will ask you to enter a permanent link for your channel. You can use lowercase letters and numbers 0-9 to create the channel link.
* Please note that the channel link name is global and you will be able to create a channel link only if the link name is available. The channel link name is something similar to an email address, i.e. only one unique email ID can exist at one time.

* Keep a note of this Channel permanent link name. It will be required later on to send messages to this channel. For example, the channel link name in the screenshot below is "temperature_alert".

![screenshot 3](/images/s3.jpeg)

* You can click on the channel name at the top to view more details about it.
* Next we will need to create and add a Bot to the channel so that it can post alerts for us in this channel.

### Create a Bot

#### What is a Bot?

Bots are third-party applications that run inside Telegram. Users can interact with bots by sending them messages, commands and requests. 

We will be using Bots to send alerts on our channel.

#### Create a new Bot

Telegram allows us to create a new bot with the help of a bot called as "BotFather". It is a single bot to create and manage other bots.

* On the Home screen of the app, click on the search icon on the top right and type in "botfather".

![screenshot 4](/images/s4.jpeg)

* In the search results, click on the correct result for "BotFather" as shown below. The correct "BotFather" will have a blue tick mark next to its name. This will take you to a chat window with the "BotFather".

![screenshot 5](/images/s5.png)

* The chat will have a few items already and will display you a list of commands to get started.
* Since we need to create a new Bot, go ahead and type in "/newbot" in the window.
* It will ask you to type in few more details like Bot name and Bot username.
* When your bot is created successfully, you will be shown a screen similar to the one below and will contain the Bot Token. This token is used to control your Bot as well as send messages on behalf of it. **Please keep this token secure as it will allow anyone to access your Bot.**
* As an example, suppose Bot token is "894346529:AAhuJ2XJQy5dlEtLYF0sc0Z_qu0fSqihSSc". Please save it as telegram_bot_id. The telegram_bot_id is saved as "bot" followed by the bot token. So, in this example, the telegram_bot_id will be "bot894346529:AAhuJ2XJQy5dlEtLYF0sc0Z_qu0fSqihSSc".
* The telegram_bot_id will be used in the python code to send messages. The python code will be taught later.
* Also, please be careful when saving the Bot ID. You may get confused between 0 and O, I and 1 etc. as they are similar looking.
* Congratulations, you have created a new Bot. Now, we will need to add it to the channel we have created previously so that we can send alerts.

#### Add the bot to channel

* From the App home screen, open the channel we have created earlier
* In the screen, click on the channel name on the top to open the information for the Channel.
* Click on the Administrators button so that we can add the newly created bot to the channel.
* Search for the bot that we have created using the Bot's username. Once you have found the correct Bot click on it to add it to the channel.** Please make sure you have clicked on the Administrators button in the previous step as this will allow our bot to post to the channel.**
* You will be asked to confirm the rights for the bot. Press on the tick mark on the top right to continue adding the bot to the channel. **Make sure that the bot has the rights to "Post Messages".**
* You will now see the newly created Bot in the list of administrators for the channel.
* Now we will code for sending messages to the channel via the Bot.

### Sending Telegram message when Bitcoin price crosses threshold

#### Understand the Price API

* To build the Bitcoin Price Alerting system, we will require a method to find the current price of Bitcoin by writing a Python program. We will use the following website https://min-api.cryptocompare.com to get the price of Bitcoin. It is a very popular site that provides APIs using which you can fetch various cryptocurrency related data. You don’t need  to create an account on the site for this assignment. On this website all currencies are called as symbols or “sym” in short. You will use the Single Symbol Price API to get the price of Bitcoin in USD. Here is the documentation of the Single Symbol Price API: https://min-api.cryptocompare.com/documentation?key=Price&cat=SingleSymbolPriceEndpoint.

* Read the API documentation to see what is the API URL you should use in your Python program as well as read about the parameters that you can need to pass to this API. You will also find the execute call button which you can click to test and see the result that the API provides. Can you now find out what will be the URL to get the price of Bitcoin in USD and INR?

* This is the API URL: https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=INR

* Replace the variables conf.py by your Bot API KEY and channel id.

#### Code 

* The python program BTCprice.py contains code which fetches Bitcoin price in INR and makes a message to the telegram channel.

* Run the BTCprice.py program to get the message.

* The program sends a message every 10 minutes. Exit the program using **CTRL+C**

* You can also replace the API Url with another Url and change the data to get the required data from the url. Also iterate the telegram message wisely to get the proper message.