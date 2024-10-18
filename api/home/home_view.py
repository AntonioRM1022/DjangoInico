from django.shortcuts import render

# Create your views here.
def home_views(requets):
    template_view="index.html"
    
    return render(requets, template_name=template_view)