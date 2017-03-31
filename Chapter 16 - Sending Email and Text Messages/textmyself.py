#! /usr/bin/env python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string

# Preset Values
accountSID = 'AC5b92b04f91e52251e549554cf7b6d831'
authToken = '0749233a957093cbe93e5b9dfa9f9532'
twilioNumber = '+441752414386'
myNumber = '+447709453720'

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_= twilioNumber, to= myNumber)
