from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Axxxxxxxxxxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "9xxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+11234567890", 
    from_="+11234567890", #your twilio number.
    body="Hi there, What's up?")

print(message.sid)
