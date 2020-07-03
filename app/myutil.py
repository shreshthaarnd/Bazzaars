from app.models import *
from django.http import HttpResponse
import csv
from datetime import date

def checkvalidity(semail):
	jdate=''
	obj=StoreData.objects.filter(Store_Email=semail)
	for x in obj:
		jdate=x.Join_Date
	jday=jdate[8:10]
	jmonth=jdate[5:7]
	jyear=jdate[0:4]
	today=date.today()
	print('hello')
	print(jdate)
	delta=today - date(int(jyear), int(jmonth), int(jday))
	days=delta.days
	if days==15:
		obj.update(Payment_Status='Unpaid')
	return days

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
			'storeemail':x.Store_Email,
			'status':x.Status,
			'complete':CheckPublishStatus2(x.Store_ID),
			'completemsg':CheckPublishStatusMsg(x.Store_ID),
	})
		url=''
		for y in x.Store_Name:
			if y!=' ':
				url=url+y
		dic.update({
			'url':url.lower(),
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

def GetShopTxnData(ordlist):
	dic={}
	lt=[]
	for x in ordlist:
		for y in OrderPaymentData.objects.filter(Order_ID=x):
			if y.TXNID!='None':
				dic={'orderid':y.Order_ID,
					'txnid':y.TXNID,
					'mode':y.PAYMENTMODE,
					'banktxnid':y.BANKTXNID,
					'bankname':y.BANKNAME,
					'txndate':y.TXNDATE,
					'respcode':y.RESPCODE,
					'respmsg':y.RESPMSG,
					'amount':y.TXNAMOUNT,
					'status':y.STATUS,
					}
				lt.append(dic)
	return lt

def GetOrderAllList(sid):
	dic={}
	lt=[]
	obj=OrderData.objects.filter(Store_ID=sid)
	for x in obj:
		dic={
			'date':x.Order_Date,
			'id':x.Order_ID,
			'uid':x.User_ID,
			'status':x.Order_Status,
			'amount':x.Order_Amount,
			'type':x.Order_Type
		}
		for y in UserAddressData.objects.filter(Address_ID=x.Address_ID):
			dic.update({'name':y.Name,
						'house':y.HouseStreet,
						'colony':y.LandmarkColony,
						'city':y.City,
						'state':y.State,
						'pincode':y.Pincode,
						'mobile':y.Mobile})
		lt.append(dic)
	return lt

def GetOrderCompletedList(sid):
	dic={}
	lt=[]
	obj=OrderData.objects.filter(Store_ID=sid, Order_Status='Completed')
	for x in obj:
		dic={
			'date':x.Order_Date,
			'id':x.Order_ID,
			'uid':x.User_ID,
			'status':x.Order_Status,
			'amount':x.Order_Amount,
			'type':x.Order_Type
		}
		for y in UserAddressData.objects.filter(Address_ID=x.Address_ID):
			dic.update({'name':y.Name,
						'house':y.HouseStreet,
						'colony':y.LandmarkColony,
						'city':y.City,
						'state':y.State,
						'pincode':y.Pincode,
						'mobile':y.Mobile})
		lt.append(dic)
	return lt

def GetOrderPendingList(sid):
	dic={}
	lt=[]
	obj=OrderData.objects.filter(Store_ID=sid, Order_Status='Pending')
	for x in obj:
		dic={
			'date':x.Order_Date,
			'id':x.Order_ID,
			'uid':x.User_ID,
			'status':x.Order_Status,
			'amount':x.Order_Amount,
			'type':x.Order_Type
		}
		for y in UserAddressData.objects.filter(Address_ID=x.Address_ID):
			dic.update({'name':y.Name,
						'house':y.HouseStreet,
						'colony':y.LandmarkColony,
						'city':y.City,
						'state':y.State,
						'pincode':y.Pincode,
						'mobile':y.Mobile})
		lt.append(dic)
	return lt

def GetOrderProducts(sid):
	obj=OrderData.objects.filter(Store_ID=sid)
	lt=[]
	dic={}
	for x in obj:
		for y in CartProductData.objects.filter(Cart_ID=x.Cart_ID):
			dic={'total':y.Product_Total,
				'quantity':y.Product_Quantity}
			for z in StoreProductData.objects.filter(Product_ID=y.Product_ID):
				dic.update({
					'name':z.Product_Name,
					'price':z.Product_Price,
					'id':z.Product_ID,
					'oid':x.Order_ID
					})
		lt.append(dic)
	return lt

def GetShopData(shopname):
	dic={}
	surl=''
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
		for s in x.Store_Name:
			if s!=' ':
				surl=surl+s
		dic.update({'url':surl.lower()})
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

def GetShopData2(sid):
	dic={}
	surl=''
	obj=StoreData.objects.filter(Store_ID=sid)
	for x in obj:
		dic={
			'storename':x.Store_Name,
			'storeaddress':x.Store_Address,
			'storecity':x.Store_City,
			'storestate':x.Store_State,
			'storemobile':x.Store_Phone,
			'storeemail':x.Store_Email
		}
		for s in x.Store_Name:
			if s!=' ':
				surl=surl+s
		dic.update({'url':surl.lower()})
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
def GetUserDatafromCart(cartid):
	dic={}
	userid=''
	for x in CartData.objects.filter(Cart_ID=cartid):
		userid=x.User_ID
		break
	for x in UserData.objects.filter(User_ID=userid):
		dic={
			'mobile':x.User_Mobile,
			'email':x.User_Email
		}
	return dic
def GetFourProducts(sid):
	dic={}
	lt=[]
	obj=StoreProductData.objects.filter(Store_ID=sid)
	for x in obj:
		dic={'id':x.Product_ID,
			'name':x.Product_Name,
			'rating':GetRating(x.Product_ID),
			'price':x.Product_Price}
		obj1=StoreProductImageData.objects.filter(Product_ID=x.Product_ID)
		for y in obj1:
			dic.update({'image':y.Product_Image.url})
			break
		lt.append(dic)
	return lt
def GetStoreIDByName(storename):
	obj=StoreData.objects.all()
	sid=''
	sname=''
	for x in obj:
		name=''
		for y in x.Store_Name:
			if y!=' ':
				name=name+y
		if name.lower()==storename:
			sid=x.Store_ID
			sname=x.Store_Name
	dic={'sid':sid,'sname':sname}
	return dic
def GetCategoryProducts(cid):
	obj=StoreProductData.objects.filter(Product_Category_ID=cid)
	dic={}
	lt=[]
	for x in obj:
		dic={'id':x.Product_ID,
			'name':x.Product_Name,
			'price':x.Product_Price,
			'rating':GetRating(x.Product_ID)}
		obj1=StoreProductImageData.objects.filter(Product_ID=x.Product_ID)
		for y in obj1:
			dic.update({'image':y.Product_Image.url})
			break
		lt.append(dic)
	return lt
def checksession(request):
	try:
		uid=request.session['userid']
		return True
	except:
		return False

def GetCartItems(obj):
	lt=[]
	for x in obj:
		dic={}
		for y in StoreProductData.objects.filter(Product_ID=x.Product_ID):
			dic={'id':y.Product_ID,
				'name':y.Product_Name,
				'price':y.Product_Price}
		for y in StoreProductImageData.objects.filter(Product_ID=x.Product_ID):
			dic.update({'image':y.Product_Image.url})
			break
		dic.update({'quantity':x.Product_Quantity,
					'tprice':x.Product_Total})
		lt.append(dic)
	return lt

def getparamdict(orderid):
	dic={}
	for x in OrderData.objects.filter(Order_ID=orderid):
		dic={
			'ORDER_ID':x.Order_ID,
			'TXN_AMOUNT':x.Order_Amount,
			'CUST_ID':x.User_ID,
			'INDUSTRY_TYPE_ID':'Retail',
			'WEBSITE':'None',
			'CHANNEL_ID':'WEB',
			'CALLBACK_URL':'https://bazzaars.com/verifypayment/'
		}
		for y in StoreData.objects.filter(Store_ID=x.Store_ID):
			storename=''
			for z in y.Store_Name:
				if z != ' ':
					storename=storename+z
			dic['WEBSITE']='WEBSTAGING'
	return dic

def getparamdict2(sid, aid):
	dic={}
	for x in StoreData.objects.filter(Store_ID=sid):
		dic={
			'ORDER_ID':aid,
			'TXN_AMOUNT':'999.00',
			'CUST_ID':x.Store_ID,
			'INDUSTRY_TYPE_ID':'Retail',
			'WEBSITE':'Bazzaars',
			'CHANNEL_ID':'WEB',
			'CALLBACK_URL':'https://bazzaars.com/verifypayment2/'
		}
		for y in StoreData.objects.filter(Store_ID=x.Store_ID):
			storename=''
			for z in y.Store_Name:
				if z != ' ':
					storename=storename+z
			dic['WEBSITE']='WEBSTAGING'
	return dic

def GetUserOrderProduct(uid):
	dic={}
	lt=[]
	obj=CartProductData.objects.filter(User_ID=uid)
	for x in obj:
		dic={'quantity':x.Product_Quantity,
			'total':x.Product_Total}
		for y in StoreProductData.objects.filter(Product_ID=x.Product_ID):
			dic.update({
				'name':y.Product_Name,
				'price':y.Product_Price
				})
		for z in StoreProductImageData.objects.filter(Product_ID=x.Product_ID):
			dic.update({
				'image':z.Product_Image.url
				})
			break
		for w in OrderData.objects.filter(Cart_ID=x.Cart_ID):
			dic.update({
				'oid':w.Order_ID
				})
		lt.append(dic)
	return lt

def GetUserOrderData(uid):
	dic={}
	lt=[]
	for x in OrderData.objects.filter(User_ID=uid, Status='Deactive'):
		dic={
		'date':x.Order_Date,
		'id':x.Order_ID,
		'status':x.Order_Status,
		'type':x.Order_Type,
		'total':x.Order_Amount,
		}
		for y in StoreData.objects.filter(Store_ID=x.Store_ID):
			dic.update({
				'storename':y.Store_Name
				})
		lt.append(dic)
	return lt

def GetUserOrderData2(uid, sid):
	dic={}
	lt=[]
	for x in OrderData.objects.filter(User_ID=uid, Store_ID=sid, Status='Deactive'):
		dic={
		'date':x.Order_Date,
		'id':x.Order_ID,
		'status':x.Order_Status,
		'type':x.Order_Type,
		}
		for y in CartProductData.objects.filter(Cart_ID=x.Cart_ID):
			dic.update({
				'quantity':y.Product_Quantity,
				'total':y.Product_Total
				})
			for z in StoreProductData.objects.filter(Product_ID=y.Product_ID):
				dic.update({
					'name':z.Product_Name,
					'pid':z.Product_ID
					})
			for w in StoreProductImageData.objects.filter(Product_ID=y.Product_ID):
				dic.update({
					'image':w.Product_Image.url
					})
		lt.append(dic)
	return lt
def GetRating(pid):
	rating=0
	obj=StoreProductRatingData.objects.filter(Product_ID=pid)
	for y in obj:
		totalrating=0
		count=0
		for x in obj:
			totalrating=totalrating+int(x.Rating)
			count=count+1
		rating=totalrating/count
	return round(rating, 1)

def GetStoreRating(sid):
	lt=[]
	ratings=[]
	for x in StoreProductData.objects.filter(Store_ID=sid):
		lt.append(x.Product_ID)
	for x in lt:
		ratings.append(GetRating(x))
	if ratings != []:
		return max(ratings)
	else:
		return 0

def CheckPublishStatus(sid):
	msg=''
	if StoreOtherData.objects.filter(Store_ID=sid).exists() == False:
		msg='Add About Your Store to Publish.'
	if StoreProductData.objects.filter(Store_ID=sid).exists() == False:
		msg='Add Product to Publish'
	if StoreProductCategoryData.objects.filter(Store_ID=sid).exists() == False:
		msg='Add Product Category to Publish'
	if StoreBannerData.objects.filter(Store_ID=sid).exists() == False:
		msg='Add Atleast One Store Banner to Publish'
	else:
		msg='Ready to Publish'
	return msg

def CheckPublishStatus2(sid):
	msg=''
	if StoreOtherData.objects.filter(Store_ID=sid).exists() == False:
		msg='100'
	if StoreSocialMedia.objects.filter(Store_ID=sid).exists() == False:
		msg='83.3'
	if StoreProductData.objects.filter(Store_ID=sid).exists() == False:
		msg='66.64'
	if StoreProductCategoryData.objects.filter(Store_ID=sid).exists() == False:
		msg='49.98'
	if StoreBannerData.objects.filter(Store_ID=sid).exists() == False:
		msg='33.33'
	if StoreMerchantData.objects.filter(Store_ID=sid).exists() == False:
		msg='16.66'
	else:
		msg='100'
	return msg

def CheckPublishStatusMsg(sid):
	msg=''
	if StoreSocialMedia.objects.filter(Store_ID=sid).exists() == False:
		msg='Add Social Media Links'
	if StoreOtherData.objects.filter(Store_ID=sid).exists() == False:
		msg='Add About Your Store to Publish.'
	if StoreProductData.objects.filter(Store_ID=sid).exists() == False:
		msg='Add Product to Publish'
	if StoreProductCategoryData.objects.filter(Store_ID=sid).exists() == False:
		msg='Add Product Category to Publish'
	if StoreBannerData.objects.filter(Store_ID=sid).exists() == False:
		msg='Add Atleast One Store Banner to Publish'
	if StoreMerchantData.objects.filter(Store_ID=sid).exists() == False:
		msg='Add Payment Merchant Credentials to Publish'
	else:
		msg='Ready to Publish'
	return msg

def DeductQuantity(cartid):
	obj=CartProductData.objects.filter(Cart_ID=cartid)
	for x in obj:
		obj1=StoreProductData.objects.filter(Product_ID=x.Product_ID)
		for y in obj1:
			stock=int(y.Product_Stock)
			oquantity=int(x.Product_Quantity)
			obj2=StoreProductData.objects.filter(Product_ID=x.Product_ID)
			obj2.update(Product_Stock=str(stock-oquantity))
	return True

def BrowseCategory(cname):
	dic={}
	lt=[]
	obj=StoreData.objects.filter(Store_Category=cname)
	for x in obj:
		dic={
		'sname':x.Store_Name,
		'scategory':x.Store_Category,
		'saddress':x.Store_Address,
		'scity':x.Store_City,
		'sstate':x.Store_State,
		'srating':GetStoreRating(x.Store_ID)
		}
		url=''
		for a in x.Store_Name:
			if a!=' ':
				url=url+a
		dic.update({
			'url':url.lower()
		})
		price=[]
		for y in StoreProductData.objects.filter(Store_ID=x.Store_ID):
			price.append(int(y.Product_Price))
		if price != []:
			dic.update({
				'sprice':min(price)
				})
		else:
			dic.update({
				'sprice':'N/A'
				})
		for z in StoreLogoData.objects.filter(Store_ID=x.Store_ID):
			dic.update({
			'slogo':z.Store_Logo.url
			})
		lt.append(dic)
	return lt

def GetSearchResults(sidlist):
	dic={}
	lt=[]
	for x in sidlist:
		obj=StoreData.objects.filter(Store_ID=x)
		for x in obj:
			dic={
			'sname':x.Store_Name,
			'scategory':x.Store_Category,
			'saddress':x.Store_Address,
			'scity':x.Store_City,
			'sstate':x.Store_State,
			'srating':GetStoreRating(x.Store_ID)
			}
			url=''
			for a in x.Store_Name:
				if a!=' ':
					url=url+a
			dic.update({
				'url':url.lower()
			})
			price=[]
			for y in StoreProductData.objects.filter(Store_ID=x.Store_ID):
				price.append(int(y.Product_Price))
			if price != []:
				dic.update({
					'sprice':min(price)
					})
			else:
				dic.update({
					'sprice':'N/A'
					})
			for z in StoreLogoData.objects.filter(Store_ID=x.Store_ID):
				dic.update({
				'slogo':z.Store_Logo.url
				})
			lt.append(dic)
	return lt

def unique(list1):
	lt=[]
	list_set = set(list1)
	unique_list = (list(list_set))
	for x in unique_list:
		lt.append(x)
	return sorted(lt)

def GetCities():
	lt=[]
	for x in StoreData.objects.all():
		lt.append(x.Store_City.upper())
	return unique(lt)

def downloaddata(table):
	if table=='FeedbackData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=FeedbackData.csv'
		writer = csv.writer(response)
		writer.writerow(["Feedback_Date", "Feedback_ID", "Name", "Email", "Feedback"])
		obj1=FeedbackData.objects.all()
		for x in obj1:
			writer.writerow([x.Feedback_Date, x.Feedback_ID, x.Name, x.Email, x.Feedback])
		return response
	if table=='AgentData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=AgentData.csv'
		writer = csv.writer(response)
		writer.writerow(["Agent_ID", "Name", "Email", "Mobile", "City"])
		obj1=AgentData.objects.all()
		for x in obj1:
			writer.writerow([x.Agent_ID, x.Name, x.Email, x.Mobile, x.City])
		return response
	if table=='StoreCategoryData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreCategoryData.csv'
		writer = csv.writer(response)
		writer.writerow(["Category_ID", "Category_Name"])
		obj1=StoreCategoryData.objects.all()
		for x in obj1:
			writer.writerow([x.Category_ID, x.Category_Name])
		return response
	if table=='StoreData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreData.csv'
		writer = csv.writer(response)
		writer.writerow(["Join_Date", "Store_ID", "Store_Name", "Store_Owner", "Store_Category", "Store_Email", "Store_Phone", "Store_Password", "Store_Address", "Store_City", "Store_State", "Verify_Status", "Status", "Payment_Status", "Payment_Status"])
		obj1=StoreData.objects.all()
		for x in obj1:
			writer.writerow([x.Join_Date, x.Store_ID, x.Store_Name, x.Store_Owner, x.Store_Category, x.Store_Email, x.Store_Phone, x.Store_Password, x.Store_Address, x.Store_City, x.Store_State, x.Verify_Status, x.Status, x.Payment_Status])
		return response
	if table=='StoreActivationData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreActivationData.csv'
		writer = csv.writer(response)
		writer.writerow(["Act_ID", "Store_ID", "CURRENCY", "GATEWAYNAME", "RESPMSG", "BANKNAME", "PAYMENTMODE", "RESPCODE", "TXNID", "TXNAMOUNT", "STATUS", "BANKTXNID", "TXNDATE", "CHECKSUMHASH"])
		obj1=StoreActivationData.objects.all()
		for x in obj1:
			writer.writerow([x.Act_ID, x.Store_ID, x.CURRENCY, x.GATEWAYNAME, x.RESPMSG, x.BANKNAME, x.PAYMENTMODE, x.RESPCODE, x.TXNID, x.TXNAMOUNT, x.STATUS, x.BANKTXNID, x.TXNDATE, x.CHECKSUMHASH])
		return response
	if table=='StoreOtherData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreOtherData.csv'
		writer = csv.writer(response)
		writer.writerow(["Store_ID", "Store_About"])
		obj1=StoreOtherData.objects.all()
		for x in obj1:
			writer.writerow([x.Store_ID, x.Store_About])
		return response
	if table=='StoreSocialMedia':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreSocialMedia.csv'
		writer = csv.wr
		iter(response)
		writer.writerow(["Store_ID", "Store_Facebook", "Store_Twitter", "Store_Instagram"])
		obj1=StoreSocialMedia.objects.all()
		for x in obj1:
			writer.writerow([x.Store_ID, x.Store_Facebook, x.Store_Twitter, x.Store_Instagram])
		return response
	if table=='StoreLogoData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreLogoData.csv'
		writer = csv.writer(response)
		writer.writerow(["Store_ID", "Store_Logo"])
		obj1=StoreLogoData.objects.all()
		for x in obj1:
			writer.writerow([x.Store_ID, x.Store_Logo])
		return response
	if table=='StoreProductCategoryData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreProductCategoryData.csv'
		writer = csv.writer(response)
		writer.writerow(["Store_ID", "Product_Category_ID", "Product_Category_Name", "Product_Category_Image"])
		obj1=StoreProductCategoryData.objects.all()
		for x in obj1:
			writer.writerow([x.Store_ID, x.Product_Category_ID, x.Product_Category_Name, x.Product_Category_Image])
		return response
	if table=='StoreProductData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreProductData.csv'
		writer = csv.writer(response)
		writer.writerow(["Store_ID", "Product_Category_ID", "Product_ID", "Product_Name", "Product_Expiry", "Product_Stock", "Product_Origin", "Product_Description", "Product_Price"])
		obj1=StoreProductData.objects.all()
		for x in obj1:
			writer.writerow([x.Store_ID, x.Product_Category_ID, x.Product_ID, x.Product_Name, x.Product_Expiry, x.Product_Stock, x.Product_Origin, x.Product_Description, x.Product_Price])
		return response
	if table=='StoreProductRatingData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreProductRatingData.csv'
		writer = csv.writer(response)
		writer.writerow(["Store_ID", "Product_ID", "Rating"])
		obj1=StoreProductRatingData.objects.all()
		for x in obj1:
			writer.writerow([x.Store_ID, x.Product_ID, x.Rating])
		return response
	if table=='StoreProductImageData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreProductImageData.csv'
		writer = csv.writer(response)
		writer.writerow(["Store_ID", "Product_Category_ID", "Product_ID", "Product_Image"])
		obj1=StoreProductImageData.objects.all()
		for x in obj1:
			writer.writerow([x.Store_ID, x.Product_Category_ID, x.Product_ID, x.Product_Image])
		return response
	if table=='StoreBannerData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreBannerData.csv'
		writer = csv.writer(response)
		writer.writerow(["Store_ID", "Store_Banner"])
		obj1=StoreBannerData.objects.all()
		for x in obj1:
			writer.writerow([x.Store_ID, x.Store_Banner])
		return response
	if table=='StoreMerchantData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=StoreMerchantData.csv'
		writer = csv.writer(response)
		writer.writerow(["Store_ID", "MID", "MERCHANT_KEY"])
		obj1=StoreMerchantData.objects.all()
		for x in obj1:
			writer.writerow([x.Store_ID, x.MID, x.MERCHANT_KEY])
		return response
	if table=='UserData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=UserData.csv'
		writer = csv.writer(response)
		writer.writerow(["User_ID", "User_Fname", "User_Lname", "User_Email", "User_Mobile", "Status", "Verify_Status"])
		obj1=UserData.objects.all()
		for x in obj1:
			writer.writerow([x.User_ID, x.User_Fname, x.User_Lname, x.User_Email, x.User_Mobile, x.Status, x.Verify_Status])
		return response
	if table=='UserAddressData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=UserAddressData.csv'
		writer = csv.writer(response)
		writer.writerow(["Address_ID", "User_ID", "Name", "HouseStreet", "LandmarkColony", "City", "State", "Pincode", "Mobile"])
		obj1=UserAddressData.objects.all()
		for x in obj1:
			writer.writerow([x.Address_ID, x.User_ID, x.Name, x.HouseStreet, x.LandmarkColony, x.City, x.State, x.Pincode, x.Mobile])
		return response
	if table=='CartData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=CartData.csv'
		writer = csv.writer(response)
		writer.writerow(["Cart_ID", "Store_ID", "User_ID", "Cart_Total", "Status"])
		obj1=CartData.objects.all()
		for x in obj1:
			writer.writerow([x.Cart_ID, x.Store_ID, x.User_ID, x.Cart_Total, x.Status])
		return response
	if table=='CartProductData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=CartProductData.csv'
		writer = csv.writer(response)
		writer.writerow(["Product_Add_Date", "Cart_ID", "Store_ID", "User_ID", "Product_ID", "Product_Quantity", "Product_Total", "Status"])
		obj1=CartProductData.objects.all()
		for x in obj1:
			writer.writerow([x.Product_Add_Date, x.Cart_ID, x.Store_ID, x.User_ID, x.Product_ID, x.Product_Quantity, x.Product_Total, x.Status])
		return response
	if table=='OrderData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=OrderData.csv'
		writer = csv.writer(response)
		writer.writerow(["Order_Date", "Order_ID", "Cart_ID", "Store_ID", "User_ID", "Address_ID", "Order_Amount", "Order_Type", "Status", "Order_Status"])
		obj1=OrderData.objects.all()
		for x in obj1:
			writer.writerow([x.Order_Date, x.Order_ID, x.Cart_ID, x.Store_ID, x.User_ID, x.Address_ID, x.Order_Amount, x.Order_Type, x.Status, x.Order_Status])
		return response
	if table=='OrderPaymentData':
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=OrderPaymentData.csv'
		writer = csv.writer(response)
		writer.writerow(["Order_ID", "MERCHANT_KEY", "CURRENCY", "RESPMSG", "BANKNAME", "PAYMENTMODE", "MID", "RESPCODE", "TXNID", "TXNAMOUNT", "STATUS", "BANKTXNID", "TXNDATE", "CHECKSUMHASH"])
		obj1=OrderPaymentData.objects.all()
		for x in obj1:
			writer.writerow([x.Order_ID, x.MERCHANT_KEY, x.CURRENCY, x.RESPMSG, x.BANKNAME, x.PAYMENTMODE, x.MID, x.RESPCODE, x.TXNID, x.TXNAMOUNT, x.STATUS, x.BANKTXNID, x.TXNDATE, x.CHECKSUMHASH])
		return response