"""se_104 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', include('smart_kitchen.urls')),
    path('homepage', include('smart_kitchen.urls')),
    
    path('khyo/', include('smart_kitchen.urls')),
    path('darnell/', include('smart_kitchen.urls')),
    path('brian/', include('smart_kitchen.urls')),
    path('jonathan/', include('smart_kitchen.urls')),
    path('srushti/', include('smart_kitchen.urls')),
	path('david/', include('smart_kitchen.urls')),
    
   
    path('/logSite/', include('smart_kitchen.urls')),
    path('sept10/', include('smart_kitchen.urls')),
    path('sept12/', include('smart_kitchen.urls')),
    path('sept16/', include('smart_kitchen.urls')),
    path('sept19/', include('smart_kitchen.urls')),
    path('sept23/', include('smart_kitchen.urls')),

    #path('invitations/', include('smart_kitchen.urls')),
    #path('creategroup/', include('smart_kitchen.urls')),
    #path('managegroup/', include('smart_kitchen.urls')),
    #path('group/', include('smart_kitchen.urls')),
    #path('editlist/', include('smart_kitchen.urls')),
    #path('list/', include('smart_kitchen.urls')),
    #path('recipe/', include('smart_kitchen.urls')),
    
    path('', include('smart_kitchen.urls')),
]
