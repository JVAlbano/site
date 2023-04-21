from django.shortcuts import render, redirect
from .models import Produto
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_user')
def dashboard(request):

    produtos = Produto.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(produtos, 3)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        'produtos': result, 
    }

    return render(request, 'dashboard.html', context)

@login_required(login_url='login_user')
def registrar_produtos(request):

    if request.method == 'POST':
        nome = request.POST.get('nome_produto')
        email = request.POST.get('email')
        preco = request.POST.get('preco_produto')
        imagem = request.FILES.get('imagem_produto')
        descricao = request.POST.get('exampleFormControlTextarea1')
        categoria = request.POST.get('basicSelect')
        print(nome)
        produto = Produto(
            nome = nome, 
            email= email, 
            preco=preco, 
            foto_produto=imagem, 
            descricao=descricao, 
            categoria=categoria
        )

        produto.save()

    return render(request, 'registrar-produtos.html')

@login_required(login_url='login_user')
def editar_produto(request, id):

    produto = Produto.objects.get(id=id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome_produto')
        email = request.POST.get('email')
        preco = request.POST.get('preco_produto')
        imagem = request.FILES.get('imagem_produto')
        descricao = request.POST.get('exampleFormControlTextarea1')
        categoria = request.POST.get('basicSelect')

        produto.nome = nome
        produto.email = email
        produto.preco = preco
        produto.foto_produto = imagem
        produto.descricao = descricao
        produto.categoria = categoria
        produto.save()

    context = {
        'produto': produto
    }

    return render(request, 'editar-produto.html')

@login_required(login_url='login_user')
def meusprodutos(request):

    produtos = Produto.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(produtos, 3)
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        'produtos': result, 
    }

    return render(request, 'meus-produtos.html', context)

@login_required(login_url='login_user')
def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('produtos')