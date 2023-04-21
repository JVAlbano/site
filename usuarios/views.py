from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib import auth

def logout(request):

    auth.logout(request)

    return redirect('login_user')

def login(request):
    if request.user.is_authenticated:
        return redirect('produtos')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if Usuario.objects.filter(user__username=username).exists():
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user=user)
                return redirect('produtos')

    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nome_completo = request.POST.get('nome_completo')
        nome = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not Usuario.objects.filter(user__email=email).exists():
            user = User.objects.create_user(username=nome, email=email,password=password, first_name=nome_completo)
            user.save()
            Usuario(user=user).save()

    return render(request, 'auth-register.html')

# Infelizmente não consegui resolver o problema com a edição de usuario
def editar_usuario(request, username):

    user = Usuario.objects.get(username=username)
    
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        password = request.POST.get('password')
        imagem = request.FILES.get('imagem')

        user.user = nome_completo
        user.email = email
        user.password = password
        user.imagem = imagem
        user.save()

    context = {
        'user': user
    }

    return render(request, 'editar-usuario.html')