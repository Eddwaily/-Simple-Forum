# -*- coding: utf-8 -*-
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8660162ce1877140c57933b5b7319750"
# Your Auth Token from twilio.com/console
auth_token  = "c57de1814695382a11bcb011dc55ebe3"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+218924346256",#the number to send a message to
    from_="+18435475071",# that's my phone number provided by tw
    body="دزلي جنيه ولا تصغر راهي متنيكة ...... محمود")

print(message.sid)
