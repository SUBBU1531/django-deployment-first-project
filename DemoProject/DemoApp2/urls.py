#"DemoApp2/urls.py" (Create a new-file)
#-------------------
#DemoApp2/urls.py

from django.urls import path;
from django.urls import re_path;

from DemoApp2 import views;

urlpatterns = [ 
	path('third/', views.f3), 
	path('fourth/', views.f4),
];
