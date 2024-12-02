from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from main.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def registro(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        registro_form = RegisterForm()

        if request.method == "POST":
            registro_form = RegisterForm(request.POST)

            if registro_form.is_valid():
                registro_form.save()
                messages.success(request,'Registro éxitoso')
                return redirect('inicio')

        return render(request, 'pages/registro.html',{
            'title': 'Registro',
            'form':registro_form,
        })
    
def login_user(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"Bienvenido al inicio de sesion")
                return redirect ('inicio')
            else:
                messages.warning(request, "No es posible el acceso ")
        return render(request, 'pages/login.html',{
            'title':'Inicio de sesion',
    })

@login_required(login_url='login')
def inicio(request):
    return render(request, 'pages/inicio.html', { 'title': 'Inicio'})

def logout_user(request):
    logout(request)
    messages.info(request,"Sesion cerrada")
    return redirect('login')
