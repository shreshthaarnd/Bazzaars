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
    path('userdashboard/',userdashboard),
    path('addaddress/',addaddress),
    path('deleteaddress/',deleteaddress),
    path('edituserdata/',edituserdata),
    
    path('shopabout/',shopabout),
    path('shopblog/',shopblog),
    path('shopblogsingle/',shopblogsingle),
    path('shopcart/',shopcart),
    path('shopcheckout/',shopcheckout),
    path('shopcontact/',shopcontact),
    path('shopindex/',shopindex),
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
    path('shoppanelpages404/',shoppanelpages404),
    path('shoppanelpages500/',shoppanelpages500),
    path('shoppaneladdproductcategory/',shoppaneladdproductcategory),
    path('shoppanelproductcategorylist/',shoppanelproductcategorylist),
    path('shoppanelproductcategorydelete/',shoppanelproductcategorydelete),
    path('saveproductcategory/',saveproductcategory),
    path('shoppanelstoreprofile/',shoppanelstoreprofile),
    path('shoppanelstorebanner/',shoppanelstorebanner),
    path('savebanner/',savebanner),
    path('shoppaneladdproduct/',shoppaneladdproduct),
    path('saveproduct/',saveproduct),
    path('shoppanelproductlist/',shoppanelproductlist),
    path('shoppanelaboutstore/',shoppanelaboutstore),
    path('savestoreabout/',savestoreabout),
    path('shoppanelstorelogo/',shoppanelstorelogo),
    path('changelogo/',changelogo),
    path('shoppanelstoresocialmedialink/',shoppanelstoresocialmedialink),
    path('savesocialmedialink/',savesocialmedialink),
    path('shoppanelpaymentsystem/',shoppanelpaymentsystem),
    path('addcategory/',addcategory),
    path('savestore/',savestore),
    path('savestorecategory/',savestorecategory),
    path('verifystore/',verifystore),
    path('resendotp/',ResendOTP),
    path('checklogin/',checklogin),
    path('checklogin2/',checklogin2),
    path('saveuser/',saveuser),
    path('verifyuser/',verifyuser),
    path('resendotpuser/',ResendOTPuser),
    path('editstoredetails/',editstoredetails),
    path('shoppanelallorderslist/',shoppanelallorderslist),
    path('shoppanelcompletedorderlist/',shoppanelcompletedorderlist),
    path('shoppanelpendingorderlist/',shoppanelpendingorderlist),
    path('<str:shopname>',storewebsite),
    path('<str:shopname>/openproductcategory/',openproductcategory),
    path('<str:shopname>/<str:pid>/',shopproductsingle),
    path('shopuserdashboard/',shopuserdashboard),
    path('searchresult/',searchresult),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

