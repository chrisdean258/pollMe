from twilio.rest import Client

def send_text(phoneNum, msg):
    account_sid = 'AC1ed7458138b80b858ef3332084a059b2'
    auth_token = '2e2e6c6b0cf2aafeb93dfc5c262e5125'
    fromNum = '+17062223470'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        phoneNum,
        body=msg,
        from_=fromNum,
    )


