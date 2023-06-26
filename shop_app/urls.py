"""
URL configuration for MYSHOP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from  shop_app.views import Home, Contact, About, ShopGrid, Checkout, ItemByCategoryView,ItemByBrandView, ProductDetail,CartItemDeleteView, CartListView, CartItemUpdateView, NewsletterView, SearchItemView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("contact/", Contact.as_view(), name="contact"),
    path("about/", About.as_view(), name="about"),
    path("detail/<int:pk>/", ProductDetail.as_view(), name="detail"),
    path("shop-grid/", ShopGrid.as_view(), name="shop-grid"),
    path("search-item/", SearchItemView.as_view(), name="search-item"),
    path("item-by-category/<int:category_id>/", ItemByCategoryView.as_view(), name="item-by-category"),
    path("item-by-brand/<int:brand_id>/", ItemByBrandView.as_view(), name="item-by-brand"),
    path("cart/", CartListView.as_view(), name="cart"),
    path("update-cart-item/<int:pk>", CartItemUpdateView.as_view(), name="update-cart-item"),
    path("checkout/", Checkout.as_view(), name="checkout"),
    path("delete-cart-item/<int:pk>/", CartItemDeleteView.as_view(), name="delete-cart-item"),
    path("newsletter/", NewsletterView.as_view(), name="newsletter"),
]

