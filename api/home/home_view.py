from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.home.value_const import LOGING_URL
# Create your views here.
@login_required (login_url=LOGING_URL)
def home_views(requets):
    template_view="index.html"
    
    return render(requets, template_name=template_view)