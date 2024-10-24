from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_view(request):
    template_name="login.html"
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            return redirect('home')
        else:
            return render (request, template_name , {'error': 'Credenciales inválidas'})
    return render(request, template_name=template_name)
# view for register.

def register_view(request):
    template_view="register.html"
    return render(request, template_name=template_view)

def logout_view(request):
    logout(request)
    return redirect('login')