from django.contrib import admin 
from django.urls import path 
from serverapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('mathserver/',views.rectarea,name="mathserver"),
    path('',views.rectarea,name="mathserverroot")
]