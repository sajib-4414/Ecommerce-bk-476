"""ecommerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from ecommerce_project.myapp import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('buyers/', views.BuyersUserAPIView.as_view()),
    path('buyers/<int:pk>/', views.BuyerDetailUpdateDeleteAPIView.as_view()),
    path('sellers/', views.SellersUserAPIView.as_view()),
    path('companies/', views.CompaniesAPIView.as_view()),
    path('addresses/', views.AddressListNCreateAPIView.as_view()),
    path('categories/', views.CategoryListNCreateAPIView.as_view()),
    path('products/', views.ProductListNCreateAPIView.as_view()),
    path('products/<int:pk>/', views.ProductDetailUpdateDeleteAPIView.as_view()),
    path('reviews/', views.ReviewListNCreateAPIView.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetailUpdateDeleteAPIView.as_view()),
    path('orders/', views.OrderListNCreateAPIView.as_view()),
    path('order-lines/', views.OrderLineListNCreateAPIView.as_view()),
    path('carts/', views.CartListNCreateAPIView.as_view()),
    path('cartlines/', views.CartLineListNCreateAPIView.as_view()),
]
