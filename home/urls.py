from django.urls import path,include 
from . import views




urlpatterns = [
   path("",views.home,name="mainapp_home"),
   path("/404/",views.notfound_page,name="page_not")
]