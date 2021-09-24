from twilio.rest import Client

account_sid = 'ACd51c35ce54dce5ec56df1da9ce74582d' # Found on Twilio Console Dashboard
auth_token = '0134a0c8d980002b045bc52be908f21d' # Found on Twilio Console Dashboard

myPhone = '+919861169611' # Phone number you used to verify your Twilio account
TwilioNumber = '+17166382342' # Phone number given to you by Twilio

client = Client(account_sid, auth_token)

client.messages.create(
  to=myPhone,
  from_=TwilioNumber,
  body='I sent a text message from Python! ' + u'\U0001f680')
