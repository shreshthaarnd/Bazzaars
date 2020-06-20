import urllib.request
import urllib.parse
 
def sendSMS(numbers, message):
    data =  urllib.parse.urlencode({'apikey': 'M231ePl4nWk-rhMFOTxzjqJW4g2qGJXmc3b5zQ7AM1',
     'sender':'BAZZRS', 
     'numbers': numbers,
     'message' : message})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
def sendOTPMessage(number, otp):
	number='91'+number
	message='Welcome to Bazzaars.com, Your verification code is '+otp
	result='sendSMS(number, message)'
	return result

def sendOrderConfirmation(number, orderid, storename, storemobile):
    number='91'+number
    message='Order Successful! with ORDER ID '+orderid+' from '+storename+'. Kindly contact Store Owner at +91 '+storemobile+' for delivery regarding issues.'
    result='sendSMS(number, message)'
    return result

def sendOrderConfirmationforStore(number, orderid, amount, customercontact):
    number='91'+number
    message='New Order Recieved! with ORDER ID '+orderid+' of amount Rs. '+amount+'. Customer Contact : +91 '+customercontact+'. Kindly contact customer for order confirmation.'
    result='sendSMS(number, message)'
    return result

def sendActivationSMS(number, storename, actid):
    number='91'+number
    message='Account Activated Successfully! Welcome to Bazzaars.com '+storename+', Activation Amount of Rs. 999/- with ACTIVATION ID '+actid+'.'
    #result=sendSMS(number, message)
    result='sendSMS(number, message)'
    return result