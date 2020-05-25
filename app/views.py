from django.shortcuts import render
from django.views.decorators.csrf import *
from app.models import *
from django.core.paginator import *
from django.core.mail import EmailMessage
from django.http import HttpResponse
import uuid

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
def shopproductsingle(request):
	return render(request,'shoppages/product-single.html',{})
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
def shoppaneldashboard(request):
	return render(request,'shoppanel/dashboard.html',{})
def shoppanelicons(request):
	return render(request,'shoppanel/icons.html',{})
def shoppanelmap(request):
	return render(request,'shoppanel/map.html',{})
def shoppanelnotifications(request):
	return render(request,'shoppanel/notifications.html',{})
def shoppanelnucleoicons(request):
	return render(request,'shoppanel/nucleo-icons.html',{})
def shoppaneltables(request):
	return render(request,'shoppanel/tables.html',{})
def shoppaneltypography(request):
	return render(request,'shoppanel/typography.html',{})
def shoppanelupgrade(request):
	return render(request,'shoppanel/upgrade.html',{})
def shoppaneluser(request):
	return render(request,'shoppanel/user.html',{})
def addcategory(request):
	for x in StoreCategoryData.objects.all():
		print(x.Category_ID)
		print(x.Category_Name)
	return HttpResponse('Saved')
@csrf_exempt
def savestore(request):
	if request.method=='POST':
		name=request.POST.get('name')
		owner=request.POST.get('owner')
		category=request.POST.get('category')
		email=request.POST.get('email')
		mobile=request.POST.get('mobile')
		s="S00"
		x=1
		sid=s+str(x)
		while StoreData.objects.filter(Store_ID=sid).exists():
			x=x+1
			sid=s+str(x)
		x=int(x)
		otp=uuid.uuid5(uuid.NAMESPACE_DNS, sid+name+owner+category+mobile+email)
		password=str(otp)
		password=password.upper()[0:6]
		obj=StoreData(
			Store_ID=sid,
			Store_Name=name,
			Store_Owner=owner,
			Store_Category=category,
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
			msg='''Hi there!
Store '''+name+''' has successfully created!

Store Password : '''+password+'''

Thanks for creating your store on Bazzaars,
Team Bazzaars'''
			sub='Congratulations! Your '+name+' Website Has Been Successfully Created'
			email=EmailMessage(sub,msg,to=[email])
			email.send()
			alert='<script type="text/javascript">alert("Your Account Has Been Successfully Created Please Check Your Mail");</script>'
			dic={'category':StoreCategoryData.objects.all(),
				'alert':alert}
			return render(request,'index.html',dic)
	else:
		return HttpResponse('<h1>Error 404 Not Found</h1>')