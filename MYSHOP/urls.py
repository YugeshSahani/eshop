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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from shop_app.views import UserRegisterView, UserLoginView, SellerLoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("shop_app.urls")),
    


    path("accounts/user-login/", UserLoginView.as_view(), name="user-login"),
    path("accounts/user-logout/", views.LogoutView.as_view(), name="user-logout"),
    path('user-registration/', UserRegisterView.as_view(), name='user-registration'),


    # path('api/', include('cart.urls')),

   
    path("accounts/seller-login/", SellerLoginView.as_view(), name="seller-login"),
    path("accounts/seller-logout/", views.LogoutView.as_view(), name="seller-logout"),
    path('seller/', include('seller_app.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
