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

def GetShopData(shopname):
	dic={}
	obj=StoreData.objects.filter(Store_Name=shopname)
	for x in obj:
		dic={
			'storename':x.Store_Name,
			'storeaddress':x.Store_Address,
			'storecity':x.Store_City,
			'storestate':x.Store_State,
			'storemobile':x.Store_Phone,
			'storeemail':x.Store_Email
		}
		obj1=StoreLogoData.objects.filter(Store_ID=x.Store_ID)
		for y in obj1:
			dic.update({
				'storelogo':y.Store_Logo.url
				})
		obj2=StoreOtherData.objects.filter(Store_ID=x.Store_ID)
		for z in obj2:
			dic.update({
				'storeabout':z.Store_About[0:200]+'....'
				})
		obj3=StoreProductCategoryData.objects.filter(Store_ID=x.Store_ID)
		d={}
		lt=[]
		for q in obj3:
			d={'id':q.Product_Category_ID,
			'name':q.Product_Category_Name,
			'image':q.Product_Category_Image.url}
			lt.append(d)
		dic.update({
			'productcategory':lt
			})
		obj4=StoreSocialMedia.objects.filter(Store_ID=x.Store_ID)
		for z in obj4:
			dic.update({
				'facebooklink':z.Store_Facebook,
				'twitterlink':z.Store_Twitter,
				'instagramlink':z.Store_Instagram,
				})
	return dic
def GetStoreIDByName(storename):
	obj=StoreData.objects.filter(Store_Name=storename)
	for x in obj:
		sid=x.Store_ID
	return sid
def GetCategoryProducts(cid):
	obj=StoreProductData.objects.filter(Product_Category_ID=cid)
	dic={}
	lt=[]
	for x in obj:
		dic={'id':x.Product_ID,
			'name':x.Product_Name,
			'price':x.Product_Price}
		obj1=StoreProductImageData.objects.filter(Product_ID=x.Product_ID)
		for y in obj1:
			dic.update({'image':y.Product_Image.url})
			break
		lt.append(dic)
	return lt