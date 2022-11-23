"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
#from .views import login,error_404,error_500,notification_firebase
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from configuracion.views import index
from .views import error_404,error_500






urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('configuracion.urlsapi')),
    path('apitux/', include('configuracion.urls')),
    path('', index.as_view() , name='index'),
    #path('', login_required(TemplateView.as_view(template_name='index.html')) , name='index'),
    
]

handler404 = error_404
handler500 = error_500

