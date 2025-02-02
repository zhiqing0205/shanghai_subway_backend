"""
URL configuration for shanghai_subway_backend project.

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
from apps.subway import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_all_data/', views.get_all_data)
]

title = '车地通信无线智能检测后台'
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = title

