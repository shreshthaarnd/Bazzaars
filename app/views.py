from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from app.models import *
from django.core.paginator import *
from django.core.mail import EmailMessage
from django.http import HttpResponse
import uuid
from app.myutil import *
import csv

# Create your views here.
def about(request):
	return render(request,'about.html',{})
def blog(request):
	return render(request,'blog.html',{})
def contact(request):
	return render(request,'contact.html',{})
def elements(request):
	return render(request,'elements.html',{})
def index(request):
	dic={'category':StoreCategoryData.objects.all(),
		'checksession':checksession(request)}
	return render(request,'index.html',dic)
def industries(request):
	return render(request,'industries.html',{})
def main(request):
	return render(request,'main.html',{})
def singleblog(request):
	return render(request,'single-blog.html',{})
def work(request):
	return render(request,'work.html',{})
def shopabout(request):
	return render(request,'shoppages/about.html',{})
def shopblog(request):
	return render(request,'shoppages/blog.html',{})
def shopblogsingle(request):
	return render(request,'shoppages/blog.html',{})
def shopcontact(request):
	return render(request,'shoppages/contact.html',{})
def shopindex(request):
	return render(request,'shoppages/index.html',{})
def shopshop(request):
	return render(request,'shoppages/shop.html',{})
def adminindex(request):
	return render(request,'adminpages/index.html',{})
def adminpagelogin(request):
	return render(request,'adminpages/page-login.html',{})
def adminpageregister(request):
	return render(request,'adminpages/page-register.html',{})
def adminpagesforget(request):
	return render(request,'adminpages/pages-forget.html',{})
def admintablesbasic(request):
	return render(request,'adminpages/tables-basic.html',{})
def admintablesdata(request):
	return render(request,'adminpages/tables-data.html',{})
def adminwidgets(request):
	return render(request,'adminpages/widgets.html',{})
def adminformsadvanced(request):
	return render(request,'adminpages/forms-advanced.html',{})
def adminformsbasic(request):
	return render(request,'adminpages/forms-basic.html',{})

def shoppanelindex(request):
	return render(request,'shoppanel/index.html',{})
def shoppanelpages404(request):
	return render(request,'shoppanel/pages-404-withoutmenus.html',{})
def shoppanelpages500(request):
	return render(request,'shoppanel/pages-500.html',{})

#Store Product Category
def shoppaneladdproductcategory(request):
	try:
		sid=request.session['storeid']
		dic=GetShopDash(sid)
		return render(request,'shoppanel/addproductcategory.html',dic)
	except:
		return redirect('/shoppanelpages404/')
@csrf_exempt
def saveproductcategory(request):
	if request.method=='POST':
		cname=request.POST.get('cname')
		cimage=request.FILES['cimage']
		sid=request.session['storeid']
		c="CA00"
		x=1
		cid=c+str(x)
		while StoreProductCategoryData.objects.filter(Product_Category_ID=cid).exists():
			x=x+1
			cid=c+str(x)
		x=int(x)
		obj=StoreProductCategoryData(
			Store_ID=sid,
			Product_Category_ID=cid,
			Product_Category_Name=cname,
			Product_Category_Image=cimage
			)
		if StoreProductCategoryData.objects.filter(Store_ID=sid, Product_Category_Name=cname).exists():
			dic={'msg':'Category Already Exists'}
			dic.update(GetShopDash(sid))
			return render(request, 'shoppanel/addproductcategory.html', dic)
		else:
			obj.save()
			dic={'msg':'Category Saved Successfully'}
			dic.update(GetShopDash(sid))
			return render(request, 'shoppanel/addproductcategory.html', dic)
	else:
		return redirect('/shoppanelpages404/')
def shoppanelproductcategorylist(request):
	try:
		sid=request.session['storeid']
		obj=StoreProductCategoryData.objects.filter(Store_ID=sid)
		dic={'data':obj}
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/productcategorylist.html',dic)
	except:
		return redirect('/shoppanelpages404/')
def shoppanelproductcategorydelete(request):
	try:
		sid=request.session['storeid']
		cid=request.GET.get('cid')
		obj=StoreProductCategoryData.objects.filter(Product_Category_ID=cid).delete()
		dic={'data':obj}
		dic.update(GetShopDash(sid))
		return redirect('/shoppanelproductcategorylist/')
	except:
		return redirect('/shoppanelpages404/')

#Store Product
def shoppaneladdproduct(request):
	try:
		sid=request.session['storeid']
		obj=StoreProductCategoryData.objects.filter(Store_ID=sid)
		dic={'data':obj}
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/addproduct.html',dic)
	except:
		return redirect('/shoppanelpages404/')
@csrf_exempt
def saveproduct(request):
	if request.method=='POST':
		sid=request.session['storeid']
		name=request.POST.get('name')
		expiry=request.POST.get('expiry')
		stock=request.POST.get('stock')
		des=request.POST.get('des')
		price=request.POST.get('price')
		images=request.FILES.getlist('images')
		category=request.POST.get('category')
		p="PR00"
		x=1
		pid=p+str(x)
		while StoreProductData.objects.filter(Product_ID=pid).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		obj=StoreProductData(
			Store_ID=sid,
			Product_Category_ID=category,
			Product_ID=pid,
			Product_Name=name,
			Product_Expiry=expiry,
			Product_Stock=stock,
			Product_Description=des,
			Product_Price=price
			)
		if StoreProductData.objects.filter(Store_ID=sid, Product_Name=name).exists():
			obj1=StoreProductCategoryData.objects.filter(Store_ID=sid)
			dic={'data':obj1,'msg':'Product Already Exists'}
			dic.update(GetShopDash(sid))
			return render(request,'shoppanel/addproduct.html',dic)
		else:
			obj.save()
			for x in images:
				print(x)
				obj2=StoreProductImageData(
					Store_ID=sid,
					Product_Category_ID=category,
					Product_ID=pid,
					Product_Image=x
					)
				obj2.save()
			obj1=StoreProductCategoryData.objects.filter(Store_ID=sid)
			dic={'data':obj1,'msg':'Product Added Successfully'}
			dic.update(GetShopDash(sid))
			return render(request,'shoppanel/addproduct.html',dic)
	else:
		return redirect('/shoppanelpages404/')

def shoppanelproductlist(request):
	try:
		sid=request.session['storeid']
		obj=StoreProductImageData.objects.all()
		for x in obj:
			print(x.Product_ID)
		dic=GetShopDash(sid)
		dic.update({'data':StoreProductData.objects.filter(Store_ID=sid)})
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/productlist.html',dic)
	except:
		return redirect('/shoppanelpages404/')

def shoppaneldeleteproduct(request):
	try:
		sid=request.session['storeid']
		pid=request.GET.get('pid')
		obj=StoreProductData.objects.filter(Product_ID=pid).delete()
		obj=StoreProductRatingData.objects.filter(Product_ID=pid).delete()
		obj=StoreProductImageData.objects.filter(Product_ID=pid).delete()
		return redirect('/shoppanelproductlist/')
	except:
		return redirect('/shoppanelpages404/')

#Store Profile
def shoppanelstoreprofile(request):
	try:
		sid=request.session['storeid']
		dic=GetShopDash(sid)
		return render(request,'shoppanel/storeprofile.html',dic)
	except:
		return redirect('/shoppanelpages404/')
	
def shoppanelstorebanner(request):
	sid=request.session['storeid']
	dic=GetShopDash(sid)
	return render(request,'shoppanel/storebanner.html',dic)
@csrf_exempt
def savebanner(request):
	if request.method=='POST':
		sid=request.session['storeid']
		banner=request.FILES['banner']
		obj=StoreBannerData(
			Store_ID=sid,
			Store_Banner=banner
			)
		obj.save()
		dic=GetShopDash(sid)
		dic.update({'msg':'Banner Uploaded'})
		return render(request,'shoppanel/storebanner.html',dic)
	else:
		return redirect('/shoppanelpages404/')

#About Store
def shoppanelaboutstore(request):
	try:
		sid=request.session['storeid']
		dic=GetShopDash(sid)
		obj=StoreOtherData.objects.filter(Store_ID=request.session['storeid'])
		dic.update({'data':obj})
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/aboutstore.html',dic)
	except:
		return redirect('/shoppanelpages404/')

@csrf_exempt
def savestoreabout(request):
	if request.method=='POST':
		about=request.POST.get('about')
		obj=StoreOtherData.objects.filter(Store_ID=request.session['storeid'])
		obj.update(Store_About=about)
		return redirect('/shoppanelaboutstore/')

#Store Logo
def shoppanelstorelogo(request):
	try:
		sid=request.session['storeid']
		obj=StoreLogoData.objects.filter(Store_ID=request.session['storeid'])
		dic={'data':obj}
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/storelogo.html',dic)
	except:
		return redirect('/shoppanelpages404/')

@csrf_exempt
def changelogo(request):
	if request.method=='POST':
		logo=request.FILES['logo']
		obj=StoreLogoData(Store_ID=request.session['storeid'],
							Store_Logo=logo)
		obj.save()
		return redirect('/shoppanelstorelogo/')

#Store Social Media Links
def shoppanelstoresocialmedialink(request):
	try:
		sid=request.session['storeid']
		obj=StoreSocialMedia.objects.filter(Store_ID=request.session['storeid'])
		dic=GetShopDash(sid)
		dic.update({'data':obj})
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/storesocialmedialink.html',dic)
	except:
		return redirect('/shoppanelpages404/')
@csrf_exempt
def savesocialmedialink(request):
	try:
		sid=request.session['storeid']
		if request.method=='POST':
			facebook=request.POST.get('facebook')
			twitter=request.POST.get('twitter')
			instagram=request.POST.get('instagram')
			obj=StoreSocialMedia.objects.filter(Store_ID=sid).delete()
			obj=StoreSocialMedia(
				Store_ID=sid,
				Store_Facebook=facebook,
				Store_Twitter=twitter,
				Store_Instagram=instagram,)
			obj.save()
			return redirect('/shoppanelstoresocialmedialink/')
	except:
		return redirect('/shoppanelpages404/')

def shoppanelpaymentsystem(request):
	try:
		sid=request.session['storeid']
		dic=GetShopDash(sid)
		obj=OrderData.objects.filter(Store_ID=sid)
		lt=[]
		tamount=0
		for x in obj:
			lt.append(x.Order_ID)
			for y in OrderPaymentData.objects.filter(Order_ID=x.Order_ID):
				if y.TXNID!='None':
					tamount=tamount+float(y.TXNAMOUNT)
		dic.update({'txndata':GetShopTxnData(reversed(list(lt))),'tamount':tamount})
		dic.update({'paydata':StoreMerchantData.objects.filter(Store_ID=sid)})
		return render(request,'shoppanel/paymentsystem.html',dic)
	except:
		return redirect('/shoppanelpages404/')

def downloadpaydata(request):
	try:
		sid=request.session['storeid']
		obj=OrderData.objects.filter(Store_ID=sid)
		lt=[]
		for x in obj:
			lt.append(x.Order_ID)
		response = HttpResponse()
		response['Content-Disposition'] = 'attachment;filename=OnlinePaymentData.csv'
		writer = csv.writer(response)
		writer.writerow(["Order Date", "Order ID", "Transaction ID", "Payment Mode", "Bank Transaction ID", "Bank Name", "Amount", "Status", "Response"])
		for x in lt:
			for y in OrderPaymentData.objects.filter(Order_ID=x):
				writer.writerow([y.TXNDATE, y.Order_ID, y.TXNID, y.PAYMENTMODE, y.BANKTXNID, y.BANKNAME, y.TXNAMOUNT, y.STATUS, y.RESPCODE+' : '+y.RESPMSG])
		return response
	except:
		return redirect('/shoppanelpages404/')

@csrf_exempt
def savestorepaymentkeys(request):
	if request.method=='POST':
		sid=request.session['storeid']
		mid=request.POST.get('MID')
		merchantkey=request.POST.get('KEY')
		if StoreMerchantData.objects.filter(Store_ID=sid):
			obj=StoreMerchantData.objects.filter(Store_ID=sid).delete()
		obj=StoreMerchantData(
			Store_ID=sid,
			MID=mid,
			MERCHANT_KEY=merchantkey
			)
		obj.save()
		return redirect('/shoppanelpaymentsystem/')
	else:
		return redirect('/shoppanelpages404/')

def addcategory(request):
	obj=StoreCategoryData.objects.all()
	for x in obj:
		print(x.Category_ID)
		print(x.Category_Name)
	return HttpResponse('Saved')

@csrf_exempt
def savestore(request):
	if request.method=='POST':
		name=request.POST.get('name')
		owner=request.POST.get('owner')
		email=request.POST.get('email')
		mobile=request.POST.get('mobile')
		password=request.POST.get('pass')
		s="S00"
		x=1
		sid=s+str(x)
		while StoreData.objects.filter(Store_ID=sid).exists():
			x=x+1
			sid=s+str(x)
		x=int(x)
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, sid+name+owner+password+mobile+email)
		otp=str(otp)
		otp=otp.upper()[0:6]
		request.session['storeotp'] = otp
		obj=StoreData(
			Store_ID=sid,
			Store_Name=name,
			Store_Owner=owner,
			Store_Email=email,
			Store_Phone=mobile,
			Store_Password=password,
			)
		if StoreData.objects.filter(Store_Name=name).exists() or StoreData.objects.filter(Store_Email=email).exists():
			alert='<script type="text/javascript">alert("Store Already exists");</script>'
			dic={'category':StoreCategoryData.objects.all(),
				'alert':alert}
			return render(request,'index.html',dic)
		else:
			obj.save()
			obj=StoreOtherData(Store_ID=sid)
			obj.save()
			msg='''Hi there!
Store '''+name+''' has successfully created! Please verify your account with the following One Time Password

Verification OTP : '''+otp+'''

Thanks for creating your store on Bazzaars,
Team Bazzaars'''
			sub='Congratulations! Your '+name+' has Successfully Created'
			email=EmailMessage(sub,msg,to=[email])
			email.send()
			alert='<script type="text/javascript">alert("Your Account Has Been Successfully Created Please Check Your Mail");</script>'
			dic={'data':StoreCategoryData.objects.all(),
				'storeid':sid}
			return render(request,'savestorecategory.html',dic)
	else:
		return HttpResponse('<h1>Error 404 Not Found</h1>')
@csrf_exempt
def savestorecategory(request):
	if request.method=='POST':
		sid=request.POST.get('storeid')
		category=request.POST.get('category')
		obj=StoreData.objects.filter(Store_ID=sid)
		obj.update(Store_Category=category)
		alert='<script type="text/javascript">alert("Your Account Has Been Successfully Created! Kindly Login to Proceed");</script>'
		dic={'category':StoreCategoryData.objects.all(),
		'alert':alert}
		dic={'storeid':sid}
		return render(request,'verifystore.html',dic)
	else:
		return HttpResponse('<h1>Error 404 Not Found</h1>')

def shoppanelpayment(request):
	return render(request,'shoppanel/payment.html',{})

@csrf_exempt
def verifystore(request):
	if request.method=='POST':
		otpp=request.POST.get('otp').upper()
		sid=request.POST.get('storeid')
		storeotp=request.session['storeotp']
		if otpp == storeotp:
			obj=StoreData.objects.filter(Store_ID=sid)
			obj.update(Verify_Status='Verified')
			request.session['storeid'] = sid
			a="ACT00"
			x=1
			aid=a+str(x)
			while StoreActivationData.objects.filter(Act_ID=aid).exists():
				x=x+1
				aid=a+str(x)
			x=int(x)
			obj=StoreActivationData(
				Act_ID=aid,
				Store_ID=sid
				)
			obj.save()
			MERCHANT_KEY = 'gDokYWVAFFW9OSlZ'
			MID = 'bAQrse69179758299775'
			data_dict = {'MID':MID}
			data_dict.update(getparamdict2(sid, aid))
			param_dict = data_dict
			param_dict['CHECKSUMHASH'] =Checksum.generateSignature(data_dict, MERCHANT_KEY)
			return render(request,'shoppanel/payment.html',param_dict)
		else:
			otp=''
			email=''
			for x in StoreData.objects.filter(Store_ID=sid):
				email=x.Store_Email
				otp=uuid.uuid5(uuid.NAMESPACE_DNS, sid+x.Store_Name+x.Store_Owner+x.Store_Category+x.Store_Phone+x.Store_Email)
			otp=str(otp)
			otp=otp.upper()[0:6]
			request.session['storeotp'] = otp
			msg='''Hi there!
Please verify your account with the following One Time Password

Verification OTP : '''+otp+'''

Thanks for creating your store on Bazzaars,
Team Bazzaars'''
			sub='Bazzaars One Time Password (OTP)'
			email=EmailMessage(sub,msg,to=[email])
			email.send()
			alert='<script type="text/javascript">alert("Incorrect OTP. We have sent another OTP, Verify Again");</script>'
			dic={'alert':alert,'storeid':sid}
			return render(request,'verifystore.html',dic)
	else:
		return HttpResponse('<h1>Error 404 Not Found</h1>')
import cgi
@csrf_exempt
def verifypayment2(request):
	MERCHANT_KEY = 'gDokYWVAFFW9OSlZ'
	CURRENCY=request.POST.get('CURRENCY')
	GATEWAYNAME=request.POST.get('GATEWAYNAME')
	RESPMSG=request.POST.get('RESPMSG')
	BANKNAME=request.POST.get('BANKNAME')
	PAYMENTMODE=request.POST.get('PAYMENTMODE')
	MID=request.POST.get('MID')
	RESPCODE=request.POST.get('RESPCODE')
	TXNID=request.POST.get('TXNID')
	TXNAMOUNT=request.POST.get('TXNAMOUNT')
	ORDERID=request.POST.get('ORDERID')
	STATUS=request.POST.get('STATUS')
	BANKTXNID=request.POST.get('BANKTXNID')
	TXNDATE=request.POST.get('TXNDATE')
	CHECKSUMHASH=request.POST.get('CHECKSUMHASH')
	respons_dict = {
					'MERCHANT_KEY':MERCHANT_KEY,
					'CURRENCY':CURRENCY,
					'GATEWAYNAME':GATEWAYNAME,
					'RESPMSG':RESPMSG,
					'BANKNAME':BANKNAME,
					'PAYMENTMODE':PAYMENTMODE,
					'MID':MID,
					'RESPCODE':RESPCODE,
					'TXNID':TXNID,
					'TXNAMOUNT':TXNAMOUNT,
					'ORDERID':ORDERID,
					'STATUS':STATUS,
					'BANKTXNID':BANKTXNID,
					'TXNDATE':TXNDATE,
					'CHECKSUMHASH':CHECKSUMHASH
	}
	checksum=respons_dict['CHECKSUMHASH']
	if 'GATEWAYNAME' in respons_dict:
		if respons_dict['GATEWAYNAME'] == 'WALLET':
			respons_dict['BANKNAME'] = 'null';
	obj=StoreActivationData.objects.filter(Act_ID=respons_dict['ORDERID']).update(
		CURRENCY=CURRENCY,
		GATEWAYNAME=GATEWAYNAME,
		RESPMSG=RESPMSG,
		BANKNAME=BANKNAME,
		PAYMENTMODE=PAYMENTMODE,
		RESPCODE=RESPCODE,
		TXNID=TXNID,
		TXNAMOUNT=TXNAMOUNT,
		STATUS=STATUS,
		BANKTXNID=BANKTXNID,
		TXNDATE=TXNDATE,
		CHECKSUMHASH=CHECKSUMHASH
		)
	MERCHANT_KEY = respons_dict['MERCHANT_KEY']
	data_dict = {'MID':respons_dict['MID']}
	data_dict.update(getparamdict(respons_dict['ORDERID']))
	checksum = Checksum.generateSignature(data_dict, MERCHANT_KEY)
	verify = Checksum.verifySignature(data_dict, MERCHANT_KEY, checksum)
	if verify:
		if respons_dict['RESPCODE'] == '01':
			obj=StoreActivationData.objects.filter(Act_ID=respons_dict['ORDERID'])
			for x in obj:
				obj1=StoreData.objects.filter(Store_ID=x.Store_ID)
				obj1.update(Payment_Status='Paid')
				request.session['storeid'] = x.Store_ID
			dic={'txndata':obj}
			dic.update({'msg':respons_dict['RESPMSG']})
			return render(request,'shoppanel/paymentsuccess.html',dic)
		else:
			obj=StoreActivationData.objects.filter(Act_ID=respons_dict['ORDERID'])
			dic={'txndata':obj}
			dic.update({'msg':respons_dict['RESPMSG']})
			return render(request,'shoppanel/paymentfailed.html',dic)
	else:
		obj=StoreActivationData.objects.filter(Act_ID=respons_dict['ORDERID'])
		dic={'txndata':obj}
		dic.update({'msg':respons_dict['RESPMSG']})
		return render(request,'shoppanel/paymentfailed.html',dic)

def ResendOTP(request):
	sid=request.GET.get('sid')
	otp=''
	email=''
	for x in StoreData.objects.filter(Store_ID=sid):
		email=x.Store_Email
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, sid+x.Store_Name+x.Store_Owner+x.Store_Category+x.Store_Phone+x.Store_Email)
	otp=str(otp)
	otp=otp.upper()[0:6]
	request.session['storeotp'] = otp
	msg='''Hi there!
Please verify your account with the following One Time Password

Verification OTP : '''+otp+'''

Thanks for creating your store on Bazzaars,
Team Bazzaars'''
	sub='Bazzaars One Time Password (OTP)'
	email=EmailMessage(sub,msg,to=[email])
	email.send()
	dic={'storeid':sid}
	return render(request,'verifystore.html',dic)

@csrf_exempt
def editstoredetails(request):
	if request.method=='POST':
		phone=request.POST.get('phone')
		address=request.POST.get('address')
		city=request.POST.get('city')
		state=request.POST.get('state')
		obj=StoreData.objects.filter(Store_ID=request.session['storeid'])
		obj.update(
			Store_Phone=phone,
			Store_Address=address,
			Store_City=city,
			Store_State=state
		)
		return redirect('/shoppanelstoreprofile/')
	else:
		return HttpResponse('<h1>Error 404 Not Found</h1>')
@csrf_exempt
def checklogin(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		dic={}
		if StoreData.objects.filter(Store_Email=email, Store_Password=password).exists():
			obj=StoreData.objects.filter(Store_Email=email)
			for x in obj:
				request.session['storeid'] = x.Store_ID
			if StoreData.objects.filter(Verify_Status='Unverified', Store_Email=email).exists():
				return redirect('/resendotp/')
			else:
				if StoreData.objects.filter(Payment_Status='Unpaid', Store_Email=email).exists():
					a="ACT00"
					x=1
					aid=a+str(x)
					while StoreActivationData.objects.filter(Act_ID=aid).exists():
						x=x+1
						aid=a+str(x)
					x=int(x)
					obj=StoreActivationData.objects.all().delete()
					obj=StoreActivationData(
						Act_ID=aid,
						Store_ID=request.session['storeid']
						)
					obj.save()
					MERCHANT_KEY = 'gDokYWVAFFW9OSlZ'
					MID = 'bAQrse69179758299775'
					data_dict = {'MID':MID}
					data_dict.update(getparamdict2(request.session['storeid'], aid))
					param_dict = data_dict
					param_dict['CHECKSUMHASH'] =Checksum.generateSignature(data_dict, MERCHANT_KEY)
					return render(request,'shoppanel/payment.html',param_dict)
				else:	
					return redirect('/shoppanelstoreprofile/')
		else:
			alert='<script type="text/javascript">alert("Incorrect Email/Password");</script>'
			dic={'category':StoreCategoryData.objects.all(),
				'alert':alert}
			return render(request,'index.html',dic)
	else:
		return HttpResponse('<h1>Error 404 Not Found</h1>')

def StorePublish(request):
	try:
		sid=request.session['storeid']
		msg=CheckPublishStatus(sid)
		if msg == 'Ready to Publish':
			obj=StoreData.objects.filter(Store_ID=sid)
			obj.update(Status='Active')
			return HttpResponse("<script>alert('Your Store has Published!'); window.location.replace('/shoppanelstoreprofile/')</script>")
		else:
			return HttpResponse("<script>alert('"+msg+"'); window.location.replace('/shoppanelstoreprofile/')</script>")
	except:
		return redirect('/shoppanelpages404/')

def StoreUnpublish(request):
	try:
		sid=request.session['storeid']
		obj=StoreData.objects.filter(Store_ID=sid)
		obj.update(Status='Deactive')
		return HttpResponse("<script>alert('Your Store has been Unpublished!'); window.location.replace('/shoppanelstoreprofile/')</script>")		
	except:
		return redirect('/shoppanelpages404/')

def shoppanelallorderslist(request):
	try:
		sid=request.session['storeid']
		dic={'alldata':reversed(GetOrderAllList(sid)),'data':GetOrderAllList(sid),'product':GetOrderProducts(sid)}
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/allorderslist.html',dic)
	except:
		return redirect('/shoppanelpages404/')

def makeordercompleted(request):
	try:
		sid=request.session['storeid']
		oid=request.GET.get('oid')
		obj=OrderData.objects.filter(Order_ID=oid)
		obj.update(Order_Status='Completed')
		return redirect('/shoppanelcompletedorderlist/')
	except:
		return redirect('/shoppanelpages404/')

def makeorderpending(request):
	try:
		sid=request.session['storeid']
		oid=request.GET.get('oid')
		obj=OrderData.objects.filter(Order_ID=oid)
		obj.update(Order_Status='Pending')
		return redirect('/shoppanelpendingorderlist/')
	except:
		return redirect('/shoppanelpages404/')

def shoppanelcompletedorderlist(request):
	try:
		sid=request.session['storeid']
		dic={'data2':GetOrderCompletedList(sid),'product':GetOrderProducts(sid),'data':reversed(GetOrderCompletedList(sid))}
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/completedorderlist.html',dic)
	except:
		return redirect('/shoppanelpages404/')

def shoppanelpendingorderlist(request):
	try:
		sid=request.session['storeid']
		dic={'data2':GetOrderPendingList(sid),'product':GetOrderProducts(sid),'data':reversed(GetOrderPendingList(sid))}
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/pendingorderlist.html',dic)
	except:
		return redirect('/shoppanelpages404/')

def storepreview(request):
	try:
		sid=request.session['storeid']
		storename=''
		for x in StoreData.objects.filter(Store_ID=sid):
			storename=x.Store_Name
		dic=GetShopData(storename)
		dic.update({
			'product':GetFourProducts(sid)[0:4],
			'banner':StoreBannerData.objects.filter(Store_ID=sid),
			'checksession':checksession(request)
			})
		return render(request,'shoppages/index.html',dic)
	except:
		return redirect('/shoppanelpages404/')

#Store Website
def storewebsite(request, shopname):
	shopname=shopname.upper()
	obj=StoreData.objects.filter(Status='Active')
	sid=''
	d=0
	storename=''
	for x in obj:
		sname=''
		for y in x.Store_Name:
			if y!=' ':
				sname=sname+y
		if shopname==sname.upper():
			sid=x.Store_ID
			storename=x.Store_Name
			d=1
	if d==1:
		dic=GetShopData(storename)
		dic.update({
			'product':GetFourProducts(sid)[0:4],
			'banner':StoreBannerData.objects.filter(Store_ID=sid),
			'checksession':checksession(request)
			})
		return render(request,'shoppages/index.html',dic)
	else:
		return HttpResponse('<h1>Error 404 Not Found</h1><br>Incorrect Store Name')

def openproductcategory(request, shopname):
	category=request.GET.get('cid')
	data1=GetStoreIDByName(shopname)
	product=GetCategoryProducts(category)
	dic=GetShopData(data1['sname'])
	page = request.GET.get('page')
	paginator = Paginator(list(reversed(product)), 15)
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)
	cname=''
	for x in StoreProductCategoryData.objects.filter(Product_Category_ID=category):
		cname=x.Product_Category_Name
	dic.update({'data':data,
				'cid':category,
				'cname':cname,
				'checksession':checksession(request),
				'categorydata':StoreProductCategoryData.objects.filter(Store_ID=data1['sid'])})
	return render(request,'shoppages/shop.html',dic)

def shopproductsingle(request, shopname, pid):
	data1=GetStoreIDByName(shopname)
	images=StoreProductImageData.objects.filter(Product_ID=pid)
	for x in images:
		print(x.Product_Image)
	productdata=StoreProductData.objects.filter(Product_ID=pid)
	dic=GetShopData(data1['sname'])
	dic.update({'images':images,
				'productdata':productdata,
				'rating':GetRating(pid),
				'checksession':checksession(request)})
	return render(request,'shoppages/product-single.html',dic)
@csrf_exempt
def saveuser(request):
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		email=request.POST.get('email')
		mobile=request.POST.get('mobile')
		password=request.POST.get('password')
		u="U00"
		x=1
		uid=u+str(x)
		while UserData.objects.filter(User_ID=uid).exists():
			x=x+1
			uid=u+str(x)
		x=int(x)
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, uid+fname+lname+password+mobile+email).int
		otp=str(otp)
		otp=otp.upper()[0:6]
		request.session['userotp'] = otp
		obj=UserData(
			User_ID=uid,
			User_Fname=fname,
			User_Lname=lname,
			User_Email=email,
			User_Mobile=mobile,
			User_Password=password
			)
		if UserData.objects.filter(User_Email=email).exists():
			return HttpResponse("<script>alert('User Already Exists'); window.location.replace('/index/')</script>")
		else:
			obj.save()
			msg='''Hi there!
Please verify your account with the following One Time Password

Verification OTP : '''+otp+'''

Thanks for creating your account on Bazzaars,
Team Bazzaars'''
			sub='Bazzaars One Time Password (OTP)'
			email=EmailMessage(sub,msg,to=[email])
			email.send()
			return render(request,'verifyuser.html',{'userid':uid})
@csrf_exempt
def verifyuser(request):
	if request.method=='POST':
		otpp=request.POST.get('otp').upper()
		uid=request.POST.get('userid')
		userotp=request.session['userotp']
		if otpp == userotp:
			obj=UserData.objects.filter(User_ID=uid)
			obj.update(Verify_Status='Verified')
			return HttpResponse("<script>alert('Account Verified Successfully. Proceed for Login'); window.location.replace('/index/')</script>")
		else:
			alert="<script>alert('Incorrect OTP');</script>"
			dic={'userid':uid,'alert':alert}
			return render(request,'verifyuser.html',dic)
	else:
		return HttpResponse('<h1>Error 404 Not Found</h1>')
def ResendOTPuser(request):
	uid=request.GET.get('uid')
	otp=request.session['userotp']
	email=''
	for x in UserData.objects.filter(User_ID=uid):
		email=x.User_Email
	msg='''Hi there!
Please verify your account with the following One Time Password

Verification OTP : '''+otp+'''

Thanks for creating your store on Bazzaars,
Team Bazzaars'''
	sub='Bazzaars One Time Password (OTP)'
	email=EmailMessage(sub,msg,to=[email])
	email.send()
	alert="<script>alert('OTP Sent Successfully!');</script>"
	dic={'userid':uid,'alert':alert}
	return render(request,'verifyuser.html',dic)
@csrf_exempt
def checklogin2(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		if UserData.objects.filter(User_Email=email,User_Password=password).exists():
			for x in UserData.objects.filter(User_Email=email):
				request.session['userid'] = x.User_ID
				break
			return redirect('/userdashboard/')
		else:
			return HttpResponse("<script>alert('Incorrect Email ID or Password'); window.location.replace('/index/')</script>")
def userdashboard(request):
#	try:
		uid=request.session['userid']
		userdata=UserData.objects.filter(User_ID=uid)
		useraddress=UserAddressData.objects.filter(User_ID=uid)
		dic={'userdata':userdata,'address':useraddress}
		dic.update({'productdata':GetUserOrderProduct(uid),
			'orderdata':GetUserOrderData(uid)})
		return render(request,'userdashboard.html',dic)
#	except:
#		return HttpResponse('<h1>Error 500 Internal Server Error</h1>')
@csrf_exempt
def edituserdata(request):
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		mobile=request.POST.get('mobile')
		uid=request.session['userid']
		obj=UserData.objects.filter(User_ID=uid).update(
			User_Fname=fname,
			User_Lname=lname,
			User_Mobile=mobile,
			)
		return redirect('/userdashboard/')
@csrf_exempt
def addaddress(request):
	if request.method=='POST':
		name=request.POST.get('name')
		house=request.POST.get('house')
		colony=request.POST.get('colony')
		city=request.POST.get('city')
		state=request.POST.get('state')
		pincode=request.POST.get('pincode')
		mobile=request.POST.get('mobile')
		a="AD00"
		x=1
		aid=a+str(x)
		while UserAddressData.objects.filter(Address_ID=aid).exists():
			x=x+1
			aid=a+str(x)
		x=int(x)
		obj=UserAddressData(
			Address_ID=aid,
			User_ID=request.session['userid'],
			Name=name,
			HouseStreet=house,
			LandmarkColony=colony,
			City=city,
			State=state,
			Pincode=pincode,
			Mobile=mobile
			)
		obj.save()
		return HttpResponse("<script>alert('Address Added Successfully'); window.location.replace('/userdashboard/')</script>")
def deleteaddress(request):
	aid=request.GET.get('aid')
	obj=UserAddressData.objects.filter(Address_ID=aid).delete()
	return HttpResponse("<script>alert('Address Deleted Successfully'); window.location.replace('/userdashboard/')</script>")
def logout(request):
	try:
		del request.session['userid']
		request.session.flush()
		return redirect('/index/')
	except:
		return redirect('/index/')
def logout2(request, shopname):
	try:
		del request.session['userid']
		request.session.flush()
		return redirect('/index/')
	except:
		return redirect('/'+shopname)
def logoutstore(request):
	try:
		del request.session['storeid']
		request.session.flush()
		return redirect('/index/')
	except:
		return redirect('/index/')
@csrf_exempt
def checklogin3(request):
	if request.method=='POST':
		shopname=request.POST.get('url')
		email=request.POST.get('email')
		password=request.POST.get('password')
		if UserData.objects.filter(User_Email=email,User_Password=password).exists():
			for x in UserData.objects.filter(User_Email=email):
				request.session['userid'] = x.User_ID
				break
			return redirect('/shopuserdashboard/?shopname='+shopname)
		else:
			return HttpResponse("<script>alert('Incorrect Email ID or Password'); window.location.replace('/index/')</script>")
def shopuserdashboard(request):
	data1=GetStoreIDByName(request.GET.get('shopname'))
	dic=GetShopData(data1['sname'])
	uid=request.session['userid']
	userdata=UserData.objects.filter(User_ID=uid)
	useraddress=UserAddressData.objects.filter(User_ID=uid)
	dic.update({'productdata':GetUserOrderData2(uid, data1['sid'])})
	dic.update({'userdata':userdata,'useraddress':useraddress})
	return render(request,'shoppages/userdashboard.html',dic)
@csrf_exempt
def saveproductrating(request):
	if request.method=='POST':
		rate=request.POST.get('stars')
		pid=request.GET.get('pid')
		print(rate)
		sname=request.GET.get('storename')
		data1=GetStoreIDByName(sname)
		if rate!=None:
			obj=StoreProductRatingData(
				Store_ID=data1['sid'],
				Product_ID=pid,
				Rating=rate
				)
			obj.save()
			return redirect('/shopuserdashboard/?shopname='+sname)
		else:
			return redirect('/shopuserdashboard/?shopname='+sname)
@csrf_exempt
def shopedituserdata(request):
	if request.method=='POST':
		fname=request.POST.get('fname')
		shopname=request.POST.get('url')
		lname=request.POST.get('lname')
		mobile=request.POST.get('mobile')
		uid=request.session['userid']
		obj=UserData.objects.filter(User_ID=uid).update(
			User_Fname=fname,
			User_Lname=lname,
			User_Mobile=mobile,
			)
		return redirect('/shopuserdashboard/?shopname='+shopname)
@csrf_exempt
def shopaddaddress(request):
	if request.method=='POST':
		shopname=request.POST.get('url')
		name=request.POST.get('name')
		house=request.POST.get('house')
		colony=request.POST.get('colony')
		city=request.POST.get('city')
		state=request.POST.get('state')
		pincode=request.POST.get('pincode')
		mobile=request.POST.get('mobile')
		a="AD00"
		x=1
		aid=a+str(x)
		while UserAddressData.objects.filter(Address_ID=aid).exists():
			x=x+1
			aid=a+str(x)
		x=int(x)
		obj=UserAddressData(
			Address_ID=aid,
			User_ID=request.session['userid'],
			Name=name,
			HouseStreet=house,
			LandmarkColony=colony,
			City=city,
			State=state,
			Pincode=pincode,
			Mobile=mobile
			)
		obj.save()
		txt="<script>alert('Address Added Successfully'); window.location.replace('/shopuserdashboard/?shopname="+shopname+"')</script>"
		return HttpResponse(txt)
def shopdeleteaddress(request):
	shopname=request.GET.get('shopname')
	aid=request.GET.get('aid')
	obj=UserAddressData.objects.filter(Address_ID=aid).delete()
	return HttpResponse("<script>alert('Address Deleted Successfully'); window.location.replace('/shopuserdashboard/?shopname="+shopname+"')</script>")
def logout2(request):
	try:
		shopname=request.GET.get('shopname')
		del request.session['userid']
		request.session.flush()
		return redirect('/'+shopname)
	except:
		return redirect('/index/')
def addtocart(request, shopname, pid):
	data1=GetStoreIDByName(shopname)
	uid=request.session['userid']
	c="CRT00"
	x=1
	cid=c+str(x)
	while CartData.objects.filter(Cart_ID=cid).exists():
		x=x+1
		cid=c+str(x)
	x=int(x)
	pprice=''
	obj=StoreProductData.objects.filter(Product_ID=pid)
	for x in obj:
		pprice=x.Product_Price
	if CartData.objects.filter(User_ID=uid, Status='Active').exists():
		cartid=''
		for x in CartData.objects.filter(User_ID=uid):
			cartid=x.Cart_ID
		if CartProductData.objects.filter(Product_ID=pid,Status='Active').exists():
			obj=CartProductData.objects.filter(Product_ID=pid)
			quantity=0
			for x in obj:
				quantity=int(x.Product_Quantity)
			quantity=quantity+1
			price=0
			obj1=StoreProductData.objects.filter(Product_ID=pid)
			for x in obj1:
				price=int(x.Product_Price)
			tprice=price*quantity
			obj.update(Product_Quantity=str(quantity),Product_Total=str(tprice))
			return HttpResponse("<script>alert('Product Added to Cart!'); window.location.replace('/"+shopname+"')</script>")
		else:
			obj=CartProductData(
				Cart_ID=cartid,
				Store_ID=data1['sid'],
				User_ID=uid,
				Product_ID=pid,
				Product_Total=pprice
			)
			obj.save()
			return HttpResponse("<script>alert('Product Added to Cart!'); window.location.replace('/"+shopname+"')</script>")
	else:
		obj=CartData(
			Cart_ID=cid,
			Store_ID=data1['sid'],
			User_ID=uid,
		)
		obj.save()
		obj=CartProductData(
			Cart_ID=cid,
			Store_ID=data1['sid'],
			User_ID=uid,
			Product_ID=pid,
			Product_Total=pprice
		)
		obj.save()
		return HttpResponse("<script>alert('Product Added to Cart!'); window.location.replace('/"+shopname+"')</script>")

def shopcart(request, shopname):
	#obj=OrderData.objects.all().delete()
	#obj=OrderPaymentData.objects.all().delete()
	#obj=CartData.objects.all().delete()
	#obj=CartProductData.objects.all().delete()
	data1=GetStoreIDByName(shopname)
	uid=request.session['userid']
	obj=CartProductData.objects.filter(User_ID=uid,Store_ID=data1['sid'],Status='Active')
	carttotal=0
	for x in obj:
		carttotal=carttotal+int(x.Product_Total)
	obj1=CartData.objects.filter(User_ID=uid,Store_ID=data1['sid'],Status='Active')
	obj1.update(Cart_Total=carttotal)
	dic=GetShopData(data1['sname'])
	dic.update({'cartdata':obj1,'cart':GetCartItems(obj),'checksession':checksession(request)})
	return render(request,'shoppages/cart.html',dic)

def addquantity(request, shopname, pid):
	data1=GetStoreIDByName(shopname)
	uid=request.session['userid']
	obj=CartProductData.objects.filter(Product_ID=pid)
	quantity=0
	tprice=0
	for x in obj:
		quantity=int(x.Product_Quantity)
	quantity=quantity+1
	price=0
	obj1=StoreProductData.objects.filter(Product_ID=pid)
	for x in obj1:
		price=int(x.Product_Price)
	tprice=price*quantity
	obj.update(Product_Quantity=str(quantity),Product_Total=str(tprice))
	obj=CartProductData.objects.filter(User_ID=uid,Store_ID=data1['sid'])
	carttotal=0
	for x in obj:
		carttotal=carttotal+int(x.Product_Total)
	obj1=CartData.objects.filter(User_ID=uid,Store_ID=data1['sid'],Status='Active')
	obj1.update(Cart_Total=carttotal)
	dic=GetShopData(data1['sname'])
	dic.update({'cartdata':obj1,'cart':GetCartItems(obj),'checksession':checksession(request)})
	return render(request,'shoppages/cart.html',dic)
def removequantity(request, shopname, pid):
	data1=GetStoreIDByName(shopname)
	uid=request.session['userid']
	obj=CartProductData.objects.filter(Product_ID=pid)
	quantity=0
	tprice=0
	for x in obj:
		quantity=int(x.Product_Quantity)
	quantity=quantity-1
	price=0
	obj1=StoreProductData.objects.filter(Product_ID=pid)
	for x in obj1:
		price=int(x.Product_Price)
	tprice=price*quantity
	obj.update(Product_Quantity=str(quantity),Product_Total=str(tprice))
	obj=CartProductData.objects.filter(User_ID=uid,Store_ID=data1['sid'])
	carttotal=0
	for x in obj:
		carttotal=carttotal+int(x.Product_Total)
	obj1=CartData.objects.filter(User_ID=uid,Store_ID=data1['sid'])
	obj1.update(Cart_Total=carttotal)
	dic=GetShopData(data1['sname'])
	dic.update({'cartdata':obj1,'cart':GetCartItems(obj),'checksession':checksession(request)})
	return render(request,'shoppages/cart.html',dic)
def selectaddress(request, shopname, crtid):
	data1=GetStoreIDByName(shopname)
	dic=GetShopData(data1['sname'])
	uid=request.session['userid']
	o="ORD00"
	x=1
	oid=o+str(x)
	while OrderData.objects.filter(Order_ID=oid).exists():
		x=x+1
		oid=o+str(x)
	x=int(x)
	if OrderData.objects.filter(Cart_ID=crtid, Status='Active').exists():
		amount=''
		for x in CartData.objects.filter(Cart_ID=crtid):
			amount=x.Cart_Total
			break
		obj=OrderData.objects.filter(Cart_ID=crtid)
		obj.update(Order_Amount=amount)
		print('hello')
		dic.update({'address':UserAddressData.objects.filter(User_ID=uid),
					'orderdata':OrderData.objects.filter(Cart_ID=crtid, Status='Active')})
		return render(request, 'shoppages/selectaddress.html', dic)
	else:
		amount=''
		for x in CartData.objects.filter(Cart_ID=crtid):
			amount=x.Cart_Total
			break
		obj=OrderData(
			Order_ID=oid,
			Cart_ID=crtid,
			Store_ID=data1['sid'],
			User_ID=uid,
			Order_Amount=amount,
			)
		obj.save()
		dic.update({'address':UserAddressData.objects.filter(User_ID=uid),
					'orderdata':OrderData.objects.filter(Order_ID=oid, Status='Active')})
		return render(request, 'shoppages/selectaddress.html', dic)
@csrf_exempt
def proceedtocheckout(request, shopname, ordid):
	if request.method=='POST':
		data1=GetStoreIDByName(shopname)
		dic=GetShopData(data1['sname'])
		aid=request.POST.get('aid')
		obj=OrderData.objects.filter(Order_ID=ordid)
		obj.update(Address_ID=aid)
		obj=OrderData.objects.filter(Order_ID=ordid)
		obj1=UserAddressData.objects.filter(Address_ID=aid)
		dic.update({'order':obj, 'address':obj1})
		request.session['sid'] = data1['sid']
		return render(request,'shoppages/checkout.html',dic)

#Paytm Payments
import app.Checksum as Checksum
import requests
import base64
import json

def order(request):
	return render(request,'shoppages/ordersuccess.html',{})

@csrf_exempt
def processpayment(request):
	if request.method=='POST':
		orderid=request.POST.get('orderid')
		paymentmode=request.POST.get('paymethod')
		obj=OrderData.objects.filter(Order_ID=orderid)
		obj.update(Order_Type=paymentmode)
		if paymentmode=='cod':
			obj=OrderData.objects.filter(Order_ID=orderid)
			obj.update(Status='Deactive')
			for x in obj:
				obj=CartData.objects.filter(Cart_ID=x.Cart_ID)
				obj.update(Status='Deactive')
				quantity=DeductQuantity(x.Cart_ID)
				obj=CartProductData.objects.filter(Cart_ID=x.Cart_ID)
				obj.update(Status='Deactive')
			sid=request.session['sid']
			dic=GetShopData2(sid)
			dic.update({'Order_ID':orderid})
			return render(request,'shoppages/ordersuccess.html',dic)
		else:
			obj=StoreMerchantData.objects.filter(Store_ID=request.session['sid'])
			MERCHANT_KEY = ''
			MID = ''
			for x in obj:
				MERCHANT_KEY = x.MERCHANT_KEY
				MID = x.MID
			data_dict = {'MID':MID}
			data_dict.update(getparamdict(orderid))
			param_dict = data_dict
			param_dict['CHECKSUMHASH'] =Checksum.generateSignature(data_dict, MERCHANT_KEY)
			return render(request,'shoppages/paymentprocess.html',param_dict)
import cgi
@csrf_exempt
def verifypayment(request):
		MERCHANT_KEY = 'gDokYWVAFFW9OSlZ'
		CURRENCY=request.POST.get('CURRENCY')
		GATEWAYNAME=request.POST.get('GATEWAYNAME')
		RESPMSG=request.POST.get('RESPMSG')
		BANKNAME=request.POST.get('BANKNAME')
		PAYMENTMODE=request.POST.get('PAYMENTMODE')
		MID=request.POST.get('MID')
		RESPCODE=request.POST.get('RESPCODE')
		TXNID=request.POST.get('TXNID')
		TXNAMOUNT=request.POST.get('TXNAMOUNT')
		ORDERID=request.POST.get('ORDERID')
		STATUS=request.POST.get('STATUS')
		BANKTXNID=request.POST.get('BANKTXNID')
		TXNDATE=request.POST.get('TXNDATE')
		CHECKSUMHASH=request.POST.get('CHECKSUMHASH')
		respons_dict = {
						'MERCHANT_KEY':MERCHANT_KEY,
						'CURRENCY':CURRENCY,
						'GATEWAYNAME':GATEWAYNAME,
						'RESPMSG':RESPMSG,
						'BANKNAME':BANKNAME,
						'PAYMENTMODE':PAYMENTMODE,
						'MID':MID,
						'RESPCODE':RESPCODE,
						'TXNID':TXNID,
						'TXNAMOUNT':TXNAMOUNT,
						'ORDERID':ORDERID,
						'STATUS':STATUS,
						'BANKTXNID':BANKTXNID,
						'TXNDATE':TXNDATE,
						'CHECKSUMHASH':CHECKSUMHASH
		}
		print(respons_dict)
		checksum=respons_dict['CHECKSUMHASH']
		if 'GATEWAYNAME' in respons_dict:
			if respons_dict['GATEWAYNAME'] == 'WALLET':
				respons_dict['BANKNAME'] = 'null';
		obj=OrderPaymentData(
			Order_ID=ORDERID,
			MERCHANT_KEY=MERCHANT_KEY,
			CURRENCY=CURRENCY,
			GATEWAYNAME=str(GATEWAYNAME),
			RESPMSG=RESPMSG,
			BANKNAME=str(BANKNAME),
			PAYMENTMODE=str(PAYMENTMODE),
			MID=MID,
			RESPCODE=RESPCODE,
			TXNID=str(TXNID),
			TXNAMOUNT=TXNAMOUNT,
			STATUS=STATUS,
			BANKTXNID=BANKTXNID,
			TXNDATE=str(TXNDATE),
			CHECKSUMHASH=CHECKSUMHASH
			)
		obj.save()
		data_dict = {'MID':respons_dict['MID']}
		data_dict.update(getparamdict(respons_dict['ORDERID']))
		checksum =Checksum.generateSignature(data_dict, MERCHANT_KEY)
		verify = Checksum.verifySignature(data_dict, MERCHANT_KEY, checksum)
		if verify:
			if respons_dict['RESPCODE'] == '01':
				obj=OrderData.objects.filter(Order_ID=ORDERID)
				obj.update(Status='Deactive')
				sid=''
				for x in obj:
					sid=x.Store_ID
					obj=CartData.objects.filter(Cart_ID=x.Cart_ID)
					obj.update(Status='Deactive')
					quantity=DeductQuantity(x.Cart_ID)
					obj=CartProductData.objects.filter(Cart_ID=x.Cart_ID)
					obj.update(Status='Deactive')
				dic=GetShopData2(sid)
				dic.update({'txndata':OrderPaymentData.objects.filter(Order_ID=ORDERID)})
				return render(request, 'shoppages/paymentsuccess.html', dic)
			else:
				obj=OrderData.objects.filter(Order_ID=ORDERID)
				obj.update(Status='Deactive')
				sid=''
				for x in obj:
					sid=x.Store_ID
					obj=CartData.objects.filter(Cart_ID=x.Cart_ID)
					obj.update(Status='Deactive')
					obj=CartProductData.objects.filter(Cart_ID=x.Cart_ID)
					obj.update(Status='Deactive')
				dic=GetShopData2(sid)
				dic.update({'txndata':OrderPaymentData.objects.filter(Order_ID=ORDERID)})
				dic.update({'because':respons_dict['RESPMSG']})
				return render(request, 'shoppages/processfail.html', dic)
		else:
			obj=OrderData.objects.filter(Order_ID=ORDERID)
			obj.update(Status='Deactive')
			sid=''
			for x in obj:
				sid=x.Store_ID
				obj=CartData.objects.filter(Cart_ID=x.Cart_ID)
				obj.update(Status='Deactive')
				obj=CartProductData.objects.filter(Cart_ID=x.Cart_ID)
				obj.update(Status='Deactive')
			dic=GetShopData2(sid)
			dic.update({'txndata':OrderPaymentData.objects.filter(Order_ID=ORDERID)})
			dic.update({'because':respons_dict['RESPMSG']})
			return render(request, 'shoppages/processfail.html', dic)


def searchresult(request):
	return render(request,'searchresult.html',{})
def shopselectaddress(request):
	return render(request,'shoppages/selectaddress.html',{})
def shoppanelpayment(request):
	return render(request,'shoppanel/payment.html',{})
def shoppanelpaymentsuccess(request):
	return render(request,'shoppanel/paymentsuccess.html',{})
def shoppanelpaymentfailed(request):
	return render(request,'shoppanel/paymentfailed.html',{})
