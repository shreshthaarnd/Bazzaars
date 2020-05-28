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
	Store_Category=models.CharField(max_length=100)
	Store_Email=models.CharField(max_length=100)
	Store_Phone=models.CharField(max_length=100)
	Store_Password=models.CharField(max_length=100)
	Store_Address=models.CharField(max_length=100, default='NA')
	Store_City=models.CharField(max_length=100, default='NA')
	Store_State=models.CharField(max_length=100, default='NA')
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
	Store_ID=models.CharField(max_length=100, primary_key=True)
	Product_Category_ID=models.CharField(max_length=100)
	Product_Category_Name=models.CharField(max_length=500)
	Product_Category_Image=models.FileField(upload_to='productcategory/')
	class Meta:
		db_table="StoreProductCategoryData"