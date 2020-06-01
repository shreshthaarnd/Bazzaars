from django.shortcuts import render, redirect
from django.views.decorators.csrf import *
from app.models import *
from django.core.paginator import *
from django.core.mail import EmailMessage
from django.http import HttpResponse
import uuid
from app.myutil import *

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
	dic={'category':StoreCategoryData.objects.all()}
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
def shopcart(request):
	return render(request,'shoppages/cart.html',{})
def shopcheckout(request):
	return render(request,'shoppages/checkout.html',{})
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
		dic=GetShopDash(sid)
		dic.update({'data':StoreProductData.objects.filter(Store_ID=sid)})
		dic.update(GetShopDash(sid))
		return render(request,'shoppanel/productlist.html',dic)
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
		return render(request,'shoppanel/paymentsystem.html',dic)
	except:
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
@csrf_exempt
def verifystore(request):
	if request.method=='POST':
		otpp=request.POST.get('otp').upper()
		sid=request.POST.get('storeid')
		storeotp=request.session['storeotp']
		if otpp == storeotp:
			obj=StoreData.objects.filter(Store_ID=sid)
			obj.update(Verify_Status='Verified')
			alert='<script type="text/javascript">alert("Your Account Has Been Successfully Created! Kindly Login to Proceed");</script>'
			dic={'category':StoreCategoryData.objects.all(),
			'alert':alert}
			return render(request,'index.html',dic)
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
			return redirect('/shoppanelstoreprofile/')
		else:
			alert='<script type="text/javascript">alert("Incorrect Email/Password");</script>'
			dic={'category':StoreCategoryData.objects.all(),
				'alert':alert}
			return render(request,'index.html',dic)
	else:
		return HttpResponse('<h1>Error 404 Not Found</h1>')
def shoppanelallorderslist(request):
	return render(request,'shoppanel/allorderslist.html',{})
def shoppanelcompletedorderlist(request):
	return render(request,'shoppanel/completedorderlist.html',{})
def shoppanelpendingorderlist(request):
	return render(request,'shoppanel/pendingorderlist.html',{})

#Store Website
def storewebsite(request, shopname):
	shopname=shopname.upper()
	obj=StoreData.objects.all()
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
			'banner':StoreBannerData.objects.filter(Store_ID=sid)
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
				'categorydata':StoreProductCategoryData.objects.filter(Store_ID=data1['sid'])})
	return render(request,'shoppages/shop.html',dic)
def userdashboard(request):
	return render(request,'userdashboard.html',{})
def shopproductsingle(request, shopname):
	data1=GetStoreIDByName(shopname)
	pid=
	return render(request,'shoppages/product-single.html',{})