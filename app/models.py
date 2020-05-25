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
	Status=models.CharField(max_length=100, default='Active')
	class Meta:
		db_table="StoreData"