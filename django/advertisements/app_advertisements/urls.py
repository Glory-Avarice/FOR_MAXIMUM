"""
URL configuration for advertisements project.

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
from django.contrib import admin
from django.urls import path
from .views import index, top_sellers, adv_post, adv_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', adv_post, name='adv-post'),
    path('advertisement/<int:pk>', adv_detail, name='adv-detail')
]