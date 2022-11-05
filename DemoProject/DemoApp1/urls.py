#"DemoApp1/urls.py" (Create a new-file)
#------------------
#DemoApp1/urls.py file

from django.urls import path;	#new
from django.urls import re_path;
from DemoApp1 import views;

urlpatterns = [ 
	path('first/', views.f1), 
	path('second/', views.f2),
];
