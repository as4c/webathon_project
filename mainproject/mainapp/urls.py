from django.contrib import admin
from django.urls import path
from . import views

app_name= 'mainapp'

urlpatterns = [
    path('home/',views.home,name='homepage'), 
    path('add/',views.add_product,name='add_product'),
    path('mysell/',views.mysell,name='mysell'),
    path('mysell/update/<int:id>',views.update_product,name='update'),
    path('mysell/delete/<int:id>',views.delete_product,name='delete'),
    path('wishlist/',views.wishlist,name='wishlist')
]

