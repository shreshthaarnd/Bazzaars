from django.db import models
import datetime
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'

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
	class Meta:
		db_table="StoreData"

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

class StoreProductImageData(models.Model):
	Store_ID=models.CharField(max_length=100)
	Product_Category_ID=models.CharField(max_length=100)
	Product_ID=models.CharField(max_length=100, primary_key=True)
	Product_Image=models.FileField(upload_to='product/')
	class Meta:
		db_table="StoreProductImageData"

class StoreBannerData(models.Model):
	Store_ID=models.CharField(max_length=100)
	Store_Banner=models.FileField(upload_to='storebanner/')
	class Meta:
		db_table="StoreBannerData"

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