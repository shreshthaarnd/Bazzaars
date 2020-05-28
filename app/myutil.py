from app.models import *

def GetShopDash(sid):
	dic={}
	obj=StoreLogoData.objects.filter(Store_ID=sid)
	for x in obj:
		dic={'storelogo':x.Store_Logo.url}
	obj=StoreData.objects.filter(Store_ID=sid)
	for x in obj:
		dic.update({
			'storename':x.Store_Name,
			'storeowner':x.Store_Owner,
			'storeaddress':x.Store_Address,
			'storecity':x.Store_City,
			'storestate':x.Store_State,
			'storephone':x.Store_Phone,
			'storeemail':x.Store_Email
	})
	obj=StoreOtherData.objects.filter(Store_ID=sid)
	for x in obj:
		dic.update({
			'about':x.Store_About[0:35]+'....'
			})
	obj=StoreSocialMedia.objects.filter(Store_ID=sid)
	for x in obj:
		dic.update({
			'facebook':x.Store_Facebook,
			'twitter':x.Store_Twitter,
			'instagram':x.Store_Instagram
			})
	return dic