from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('info',views.info,name='info'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('details',views.details,name='details'),
    path('Login',views.log,name='log'),
    path('Logout',views.logo,name='logo'),
    path('regist',views.register_user,name="register"),
    path('products/<int:pk>',views.product,name="product"),
    path('cart',views.cart,name="cart"),
    path('Addcart/<int:pk>/',views.Addcart,name="Addcart"),
    path('categories/<str:foo>',views.category,name="category"),
    path('Addagents',views.addhtml,name="AddHtml"),
    path('agents',views.agents,name="agents"),
]