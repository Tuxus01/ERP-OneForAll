from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler400, handler403, handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from .views import *



app_name='base2'

urlpatterns = [
    #path('', index , name="index"),
    path('CategoryAxios', CategoryAxios , name="CategoryAxios"),
    path('SubCategoryAxios', SubCategoryAxios , name="SubCategoryAxios"),
    path('ColorsAxios', ColorsAxios , name="ColorsAxios"),
    path('BinAxios', BinAxios , name="BinAxios"),
    path('ComponentAxios', ComponentAxios , name="ComponentAxios"),
    path('UnitsAxios', UnitsAxios , name="UnitsAxios"),
    path('WarehouseAxios', WarehouseAxios , name="WarehouseAxios"),
    path('MaterialAxios', MaterialAxios , name="MaterialAxios"),
    path('SavePOManualAxios', SavePOManualAxios , name="SavePOManualAxios"),

]