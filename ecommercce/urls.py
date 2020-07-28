
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index),
    path('addUser',v.addUser),
    path('productList',v.productList),
    path('login',v.user_login),
    path('getProductByCategory',v.getProductByCategory),
    path('searchProduct',v.searchProduct),
    path('logout',v.user_logout),
    path('addToCart',v.addToCart),
    path('cartList',v.cartList),
    path('deleteProduct_userCart//<int:id>',v.deleteProduct_userCart),
    path('editProfile',v.editProfile),
    path('myOrder',v.myOrder),
    path('imagedata',v.imagedata),
]
