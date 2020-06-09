import urllib.request
import urllib.parse
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS('M231ePl4nWk-rhMFOTxzjqJW4g2qGJXmc3b5zQ7AM1', '918938979011',
    'Bazzaars', 'Hi Sonali Kaam pe aa jao')
print (resp)