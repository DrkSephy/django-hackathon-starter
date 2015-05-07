# pylint: disable=invalid-name
# pylint: disable=unused-variable

'''
Twilioapi.py is responsible for sending
a message from a registered Twilio number
to a user's phone.
'''
from twilio.rest import TwilioRestClient

account_sid = "AC7889a1889c1833bd7181e45e60372776"
auth_token = "1ad0315f3cc7a154aaaef048f1304f71"
client = TwilioRestClient(account_sid, auth_token)

def sendSMS(body, to, sender):

    '''Sends a message to a given number'''
    message = client.messages.create(body=body, to=to, from_=sender)
    return
