from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Carrinho, Produto, ProdutoCarrinho, Cliente, ProdutoCarrinho, Estoque
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ClienteForm

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
    print(produtos)
    print(produtos)
    return render(request, 'homepage.html', {'produtos': produtos})

def cadastro_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print(form)
        if form.is_valid():
            # Criando o usuário
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
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
    produto = get_object_or_404(Produto, id=codigo)

    # Adicione o produto ao carrinho (ou aumente a quantidade)
    produto_carrinho, created = ProdutoCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
    )

    if not created:
        produto_carrinho.quantidade += 1
        produto_carrinho.save()

    return redirect(carrinho_view)  # Redireciona para a página do carrinho


@login_required
def carrinho_view(request):
    cliente = Cliente.objects.get(user=request.user)
    carrinho = Carrinho.objects.filter(cliente=cliente).first()
    itens = carrinho.produtocarrinho_set.all() if carrinho else []
    return render(request, 'carrinho.html', {'carrinho': carrinho, 'itens': itens})

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

def finalizar_compra():
    return redirect('homepage')