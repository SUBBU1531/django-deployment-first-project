from django.shortcuts import render
from django.http import HttpResponse;

#===>>> Single project with multiple applications::- 
# Create your views here.

def f11(request): 
	return HttpResponse("<h2>Hello, Good Morning User..!! Have a Nice day...</h2><hr/>");
    