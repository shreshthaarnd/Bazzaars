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
    path('logoutuser/',logout),
    path('logout/',logoutstore),
    
    path('shopabout/',shopabout),
    path('shopblog/',shopblog),
    path('shopblogsingle/',shopblogsingle),
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

    path('storepublish/',StorePublish),
    path('storeunpublish/',StoreUnpublish),
    path('storepreview/',storepreview),
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
    path('deleteproduct/',shoppaneldeleteproduct),
    path('shoppanelaboutstore/',shoppanelaboutstore),
    path('savestoreabout/',savestoreabout),
    path('shoppanelstorelogo/',shoppanelstorelogo),
    path('changelogo/',changelogo),
    path('shoppanelstoresocialmedialink/',shoppanelstoresocialmedialink),
    path('savesocialmedialink/',savesocialmedialink),
    path('shoppanelpaymentsystem/',shoppanelpaymentsystem),
    path('downloadpaydata/',downloadpaydata),
    path('savestorepaymentkeys/',savestorepaymentkeys),
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
    path('makeordercompleted/',makeordercompleted),
    path('makeorderpending/',makeorderpending),
    path('shoppanelcompletedorderlist/',shoppanelcompletedorderlist),
    path('shoppanelpendingorderlist/',shoppanelpendingorderlist),
    path('<str:shopname>',storewebsite),
    path('<str:shopname>/openproductcategory/',openproductcategory),
    path('<str:shopname>/<str:pid>/',shopproductsingle),
    path('checklogin3/',checklogin3),
    path('shopuserdashboard/',shopuserdashboard),
    path('shopedituserdata/',shopedituserdata),
    path('shopaddaddress/',shopaddaddress),
    path('shopdeleteaddress/',shopdeleteaddress),
    path('logout2/',logout2),
    path('searchresult/',searchresult),
    path('shoppanelpayment/',shoppanelpayment),

    path('shoppanelpaymentsuccess/',shoppanelpaymentsuccess),
    path('shoppanelpaymentfailed/',shoppanelpaymentfailed),

    path('paymentprocess/',processpayment),
    path('verifypayment/',verifypayment),
    path('verifypayment2/',verifypayment2),

    path('order/',order),
    path('adminlogin/',adminlogin),
    path('adminstoreslist/',adminstoreslist),
    path('adminpublishedstore/',adminpublishedstore),
    path('adminunpublishedstore/',adminunpublishedstore),
    path('admindeactivestore/',admindeactivestore),
    path('adminunverifiedstore/',adminunverifiedstore),
    path('adminpaidstores/',adminpaidstores),
    path('adminunpaidstores/',adminunpaidstores),
    path('adminstoremerchantdata/',adminstoremerchantdata),
    path('adminstoreactivationdata/',adminstoreactivationdata),
    path('adminorderlist/',adminorderlist),
    path('adminonlinepaidorderlist/',adminonlinepaidorderlist),
    path('admincodorderlist/',admincodorderlist),
    path('admincompleteorderlist/',admincompleteorderlist),
    path('adminincompleteorderlist/',adminincompleteorderlist),
    path('adminorderpaymentdata/',adminorderpaymentdata),
    path('admindeactiveuser/',admindeactiveuser),
    path('adminactiveuser/',adminactiveuser),
    path('adminuseraddressdata/',adminuseraddressdata),
    path('adminaddcategory/',adminaddcategory),
    path('adminlistcategory/',adminlistcategory),
    path('termscondition/',termscondition),

    path('<str:shopname>/addtocart/<str:pid>/',addtocart),
    path('<str:shopname>/addquantity/<str:pid>/',addquantity),
    path('<str:shopname>/removequantity/<str:pid>/',removequantity),
    path('<str:shopname>/shopcart/opencart/',shopcart),
    path('saverating/',saveproductrating),
    path('<str:shopname>/<str:crtid>/selectaddress/',selectaddress),
    path('<str:shopname>/<str:ordid>/proceedtocheckout/',proceedtocheckout),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

