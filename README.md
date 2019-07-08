# Price Tracker with Telegram
A small script to track price of a product in Amazon.in and send the price in your telegram app if price drops

## Creating your bot
To get message on your telegram you will have to create a bot first.
1. On Telegram, search @ BotFather, click on start or send him a “/start” message
2. Send another “/newbot” message, create your new bot.
3. Here copy your HTTP API, this will be used in your script.
4. On Telegram, search your bot (by the username you just created), press the “Start” button or send a “/start” message.
5. Open a new tab with your browser, enter ```https://api.telegram.org/bot<yourtoken>/getUpdates``` , replace <yourtoken> with your API token, press enter and you should see something like this:
  
```
        {"ok":true,"result":[{"update_id":77xxxxxxx,
      "message":{"message_id":550,"from":{"id":34xxxxxxx,"is_bot":false,"first_name":"ManHay","last_name":"Hong","username":"manhay212","language_code":"en-HK"}

```
###### Note: To get something like this you will have to add your bot to any of the group of yours.

6. Afterwards just fill bot_token = 'HTTP API that you got, bot_chatID = 'id that you got from your browser'
7. Run your script with the price you want to send.

For the test purpose I have added oneplus 7 price where you can add anything of your choice and you can run a scheduler which will send you the price every day or week.

In our script we can add multiple checks to see if the amount has dropped as per our requirement
