import twilio
from twilio.rest import TwilioRestClient
 
account_sid = "AC7889a1889c1833bd7181e45e60372776"
auth_token  = "1ad0315f3cc7a154aaaef048f1304f71"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi DrkSephy",
    to="+13473282978",
    from_="+13473781813") 

