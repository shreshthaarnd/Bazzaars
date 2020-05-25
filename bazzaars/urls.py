"""bazzaars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about),
    path('blog/',blog),
    path('contact/',contact),
    path('elements/',elements),
    path('index/',index),
    path('industries/',industries),
    path('main/',main),
    path('singleblog/',singleblog),
    path('work/',work),
    path('shopabout/',shopabout),
    path('shopblog/',shopblog),
    path('shopblogsingle/',shopblogsingle),
    path('shopcart/',shopcart),
    path('shopcheckout/',shopcheckout),
    path('shopcontact/',shopcontact),
    path('shopindex/',shopindex),
    path('shopproductsingle/',shopproductsingle),
    path('shopshop/',shopshop),
    path('adminindex/',adminindex),
    path('adminpagelogin/',adminpagelogin),
    path('adminpageregister/',adminpageregister),
    path('adminpagesforget/',adminpagesforget),
    path('admintablesbasic/',admintablesbasic),
    path('admintablesdata/',admintablesdata),
    path('adminwidgets/',adminwidgets),
    path('adminformsadvanced/',adminformsadvanced),
    path('adminformsbasic/',adminformsbasic),
    path('shoppanelindex/',shoppanelindex),
    path('shoppanelbooklist/',shoppanelbooklist),
    path('shoppanelpages404/',shoppanelpages404),
    path('shoppanelpages500/',shoppanelpages500),
    path('shoppanelpostnews/',shoppanelpostnews),
]
