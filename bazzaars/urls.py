from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

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
    path('shoppaneladdproductcategory/',shoppaneladdproductcategory),
    path('shoppanelaboutshop/',shoppanelaboutshop),
    path('shoppanelstoreprofile/',shoppanelstoreprofile),


    path('addcategory/',addcategory),
    path('savestore/',savestore),
    path('checklogin/',checklogin),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

