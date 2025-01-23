from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Carrinho, Produto, ProdutoCarrinho, Cliente, Pagamento, Pedido, PedidoProduto
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm
from django.utils import timezone

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin/')  # Admins vão para o painel administrativo
            else:
                return redirect('/homepage/')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas!'})

    return render(request, 'login.html')

def homepage_view(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'homepage.html', {'produtos': produtos})

def cadastro_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = request.POST['confirm_password']

            # Verificar se as senhas coincidem
            if password != confirm_password:
                return render(request, 'cadastro.html', {'form': form, 'error': 'As senhas não coincidem!'})

            # Criando o usuário
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=password
            )
            
            # Criando o cliente vinculado ao usuário
            cliente = form.save(commit=False)
            cliente.user = user
            cliente.save()

            return redirect('login')  # Redireciona para a página de login
    else:
        form = ClienteForm()
    return render(request, 'cadastro.html', {'form': form})

@login_required
def adicionar_ao_carrinho(request, codigo):
    cliente = request.user.cliente

    # Obtenha ou crie o carrinho para este cliente
    carrinho, created = Carrinho.objects.get_or_create(cliente=cliente)

    # Obtenha o produto a ser adicionado
    produto = get_object_or_404(Produto, codigo=codigo)

    # Adicione o produto ao carrinho (ou aumente a quantidade)
    produto_carrinho, created = ProdutoCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
    )

    if created:
        # Se o produto foi criado, inicialize a quantidade como 1
        produto_carrinho.quantidade = 1
        produto_carrinho.save()
    else:
        # Caso contrário, apenas aumente a quantidade
        produto_carrinho.quantidade += 1
        produto_carrinho.save()

    return redirect(carrinho_view)  # Redireciona para a página do carrinho

@login_required
def carrinho_view(request):
    cliente = Cliente.objects.get(user=request.user)
    carrinho = Carrinho.objects.filter(cliente=cliente).first()
    itens = carrinho.produtocarrinho_set.all() if carrinho else []

    # Calcular o total geral
    total_geral = sum(item.produto.preco * item.quantidade for item in itens)

    return render(request, 'carrinho.html', {'carrinho': carrinho, 'itens': itens, 'total_geral': total_geral})


def diminuir_quantidade(request, codigo):
    cliente = request.user.cliente  # Assumindo que cada usuário está vinculado a um cliente
    item = get_object_or_404(ProdutoCarrinho, produto__codigo=codigo, carrinho__cliente=cliente)

    # Diminui a quantidade ou remove o item se a quantidade for 1
    if item.quantidade > 1:
        item.quantidade -= 1
        item.save()
    else:
        item.delete()
    return redirect('carrinho')


def aumentar_quantidade(request, codigo):
    cliente = request.user.cliente  # Assumindo que cada usuário está vinculado a um cliente
    item = get_object_or_404(ProdutoCarrinho, produto__codigo=codigo, carrinho__cliente=cliente)

    item.quantidade += 1
    item.save()

    return redirect('carrinho')

@login_required
def finalizar_compra(request):
    cliente = Cliente.objects.get(user=request.user)
    carrinho = Carrinho.objects.filter(cliente=cliente).first()
    itens = carrinho.produtocarrinho_set.all() if carrinho else []
    total_geral = sum(item.produto.preco * item.quantidade for item in itens)

    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        endereco = request.POST.get('endereco')
        metodo_pagamento = request.POST.get('metodo_pagamento')

        # Criar o pedido
        pedido = Pedido.objects.create(
            cliente=cliente,
            valor=total_geral,
            status='Pendente'
        )

        # Adicionar produtos ao pedido
        for item in itens:
            PedidoProduto.objects.create(
                pedido=pedido,
                produto=item.produto,
                quantidade=item.quantidade
            )

        # Registrar o pagamento
        Pagamento.objects.create(
            pedido=pedido,
            metodo=metodo_pagamento
        )

        # Esvaziar o carrinho
        carrinho.produtocarrinho_set.all().delete()

        return redirect('homepage')  # Redireciona para a homepage após finalizar o pedido

    return render(request, 'finalizar_compra.html', {
        'cliente': cliente,
        'itens': itens,
        'total_geral': total_geral
    })

def remover_do_carrinho(request, codigo):
    cliente = request.user.cliente  # Assumindo que cada usuário está vinculado a um cliente
    item = get_object_or_404(ProdutoCarrinho, produto__codigo=codigo, carrinho__cliente=cliente)

    # Remove o item do carrinho
    item.delete()

    return redirect('carrinho')