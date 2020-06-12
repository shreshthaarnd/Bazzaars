from django.db import models
from datetime import date
from django.conf import settings


class FeedbackData(models.Model):
	Feedback_Date=models.CharField(max_length=15, default=date.today().strftime("%d/%m/%Y"))
	Feedback_ID=models.CharField(max_length=20, primary_key=True)
	Name=models.CharField(max_length=50)
	Email=models.CharField(max_length=50)
	Feedback=models.CharField(max_length=500)
	class Meta:
		db_table="FeedbackData"

class AgentData(models.Model):
	Agent_ID=models.CharField(max_length=20, primary_key=True)
	Name=models.CharField(max_length=50)
	Email=models.CharField(max_length=50)
	Mobile=models.CharField(max_length=50)
	City=models.CharField(max_length=50)
	class Meta:
		db_table="AgentData"

class StoreCategoryData(models.Model):
	Category_ID=models.CharField(max_length=100, primary_key=True)
	Category_Name=models.CharField(max_length=100)
	class Meta:
		db_table="StoreCategoryData"

class StoreData(models.Model):
	Store_ID=models.CharField(max_length=100, primary_key=True)
	Store_Name=models.CharField(max_length=100)
	Store_Owner=models.CharField(max_length=100)
	Store_Category=models.CharField(max_length=100, default='NA')
	Store_Email=models.CharField(max_length=100)
	Store_Phone=models.CharField(max_length=100)
	Store_Password=models.CharField(max_length=100)
	Store_Address=models.CharField(max_length=100, default='NA')
	Store_City=models.CharField(max_length=100, default='NA')
	Store_State=models.CharField(max_length=100, default='NA')
	Verify_Status=models.CharField(max_length=100, default='Unverified')
	Status=models.CharField(max_length=100, default='Deactive')
	Payment_Status=models.CharField(max_length=100, default='Unpaid')
	class Meta:
		db_table="StoreData"

class StoreActivationData(models.Model):
	Act_ID=models.CharField(max_length=100, primary_key=True)
	Store_ID=models.CharField(max_length=100)
	CURRENCY=models.CharField(max_length=100, default='None')
	GATEWAYNAME=models.CharField(max_length=100, default='None')
	RESPMSG=models.CharField(max_length=1000, default='None')
	BANKNAME=models.CharField(max_length=100, default='None')
	PAYMENTMODE=models.CharField(max_length=100, default='None')
	RESPCODE=models.CharField(max_length=100, default='None')
	TXNID=models.CharField(max_length=100, default='None')
	TXNAMOUNT=models.CharField(max_length=100, default='None')
	STATUS=models.CharField(max_length=100, default='None')
	BANKTXNID=models.CharField(max_length=100, default='None')
	TXNDATE=models.CharField(max_length=100, default='None')
	CHECKSUMHASH=models.CharField(max_length=100, default='None')
	class Meta:
		db_table="StoreActivationData"

class StoreOtherData(models.Model):
	Store_ID=models.CharField(max_length=100, primary_key=True)
	Store_About=models.CharField(max_length=1500, default='NA')
	class Meta:
		db_table="StoreOtherData"

class StoreSocialMedia(models.Model):
	Store_ID=models.CharField(max_length=100, primary_key=True)
	Store_Facebook=models.CharField(max_length=500, default='NA')
	Store_Twitter=models.CharField(max_length=500, default='NA')
	Store_Instagram=models.CharField(max_length=500, default='NA')
	class Meta:
		db_table="StoreSocialMedia"

class StoreLogoData(models.Model):
	Store_ID=models.CharField(max_length=100, primary_key=True)
	Store_Logo=models.FileField(upload_to='storelogo/')
	class Meta:
		db_table="StoreLogoData"

class StoreProductCategoryData(models.Model):
	Store_ID=models.CharField(max_length=100)
	Product_Category_ID=models.CharField(max_length=100, primary_key=True)
	Product_Category_Name=models.CharField(max_length=500)
	Product_Category_Image=models.FileField(upload_to='productcategory/')
	class Meta:
		db_table="StoreProductCategoryData"

class StoreProductData(models.Model):
	Store_ID=models.CharField(max_length=100)
	Product_Category_ID=models.CharField(max_length=100)
	Product_ID=models.CharField(max_length=100, primary_key=True)
	Product_Name=models.CharField(max_length=500)
	Product_Expiry=models.CharField(max_length=500, default="NA")
	Product_Stock=models.CharField(max_length=500, default="NA")
	Product_Description=models.CharField(max_length=1000, default='Description Not Availiable')
	Product_Price=models.CharField(max_length=100)
	class Meta:
		db_table="StoreProductData"

class StoreProductRatingData(models.Model):
	Store_ID=models.CharField(max_length=100)
	Product_ID=models.CharField(max_length=100)
	Rating=models.CharField(max_length=100, default="0")
	class Meta:
		db_table="StoreProductRatingData"

class StoreProductImageData(models.Model):
	Store_ID=models.CharField(max_length=100)
	Product_Category_ID=models.CharField(max_length=100)
	Product_ID=models.CharField(max_length=100)
	Product_Image=models.FileField(upload_to='product/')
	class Meta:
		db_table="StoreProductImageData"

class StoreBannerData(models.Model):
	Store_ID=models.CharField(max_length=100)
	Store_Banner=models.FileField(upload_to='storebanner/')
	class Meta:
		db_table="StoreBannerData"

class StoreMerchantData(models.Model):
	Store_ID=models.CharField(max_length=100)
	MID=models.CharField(max_length=500)
	MERCHANT_KEY=models.CharField(max_length=500)
	class Meta:
		db_table="StoreMerchantData"

class UserData(models.Model):
	User_ID=models.CharField(max_length=100, primary_key=True)
	User_Fname=models.CharField(max_length=100)
	User_Lname=models.CharField(max_length=100)
	User_Email=models.CharField(max_length=150)
	User_Mobile=models.CharField(max_length=100)
	User_Password=models.CharField(max_length=50)
	Status=models.CharField(max_length=50, default='Active')
	Verify_Status=models.CharField(max_length=50, default='Unverified')
	class Meta:
		db_table="UserData"

class UserAddressData(models.Model):
	Address_ID=models.CharField(max_length=100, primary_key=True)
	User_ID=models.CharField(max_length=100)
	Name=models.CharField(max_length=100)
	HouseStreet=models.CharField(max_length=100)
	LandmarkColony=models.CharField(max_length=100)
	City=models.CharField(max_length=100)
	State=models.CharField(max_length=100)
	Pincode=models.CharField(max_length=100)
	Mobile=models.CharField(max_length=100)
	class Meta:
		db_table="UserAddressData"

class CartData(models.Model):
	Cart_ID=models.CharField(max_length=100, primary_key=True)
	Store_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100)
	Cart_Total=models.CharField(max_length=100, default='0')
	Status=models.CharField(max_length=50, default='Active')
	class Meta:
		db_table="CartData"

class CartProductData(models.Model):
	Product_Add_Date=models.CharField(max_length=50, default=date.today().strftime("%d/%m/%Y"))
	Cart_ID=models.CharField(max_length=100)
	Store_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100)
	Product_ID=models.CharField(max_length=100)
	Product_Quantity=models.CharField(max_length=100, default='1')
	Product_Total=models.CharField(max_length=100, default='0')
	Status=models.CharField(max_length=50, default='Active')
	class Meta:
		db_table="CartProductData"

class OrderData(models.Model):
	Order_Date=models.CharField(max_length=50, default=date.today().strftime("%d/%m/%Y"))
	Order_ID=models.CharField(max_length=100)
	Cart_ID=models.CharField(max_length=100)
	Store_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100)
	Address_ID=models.CharField(max_length=100, default='NA')
	Order_Amount=models.CharField(max_length=100)
	Order_Type=models.CharField(max_length=100, default='NA')
	Status=models.CharField(max_length=50, default='Active')
	Order_Status=models.CharField(max_length=50, default='Pending')
	class Meta:
		db_table="OrderData"

class OrderPaymentData(models.Model):
	Order_ID=models.CharField(max_length=100, default='None', blank=True)
	MERCHANT_KEY=models.CharField(max_length=100, default='None', blank=True)
	CURRENCY=models.CharField(max_length=100, default='None', blank=True)
	GATEWAYNAME=models.CharField(max_length=100, default='None', blank=True)
	RESPMSG=models.CharField(max_length=1000, default='None', blank=True)
	BANKNAME=models.CharField(max_length=100, default='None', blank=True)
	PAYMENTMODE=models.CharField(max_length=100, default='None', blank=True)
	MID=models.CharField(max_length=100, default='None', blank=True)
	RESPCODE=models.CharField(max_length=100, default='None', blank=True)
	TXNID=models.CharField(max_length=100, default='None', blank=True)
	TXNAMOUNT=models.CharField(max_length=100, default='None', blank=True)
	STATUS=models.CharField(max_length=100, default='None', blank=True)
	BANKTXNID=models.CharField(max_length=100, default='None', blank=True)
	TXNDATE=models.CharField(max_length=100, default='None', blank=True)
	CHECKSUMHASH=models.CharField(max_length=100, default='None', blank=True)
	class Meta:
		db_table="OrderPaymentData"