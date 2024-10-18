from django.shortcuts import render

# Create your views here.
def login_view(requets):
    template_view="lauth-login.html"
    
    return render(requets, template_name=template_view)