from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email = models.EmailField(unique = True)
    telefone = models.CharField(max_length=15)
    dataNasc = models.DateField()
    

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=5, unique = True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits = 10, decimal_places = 2)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, related_name = "pedidos")
    produto = models.ManyToManyField(Produto, through = 'PedidoProduto', related_name = "pedidos")
    valor = models.DecimalField(max_digits = 10, decimal_places = 2)
    data = models.DateField(auto_now_add = True)
    status = models.CharField(max_length=10,choices = [('Pendente', 'Pendente'), ('Pago', 'Pago'), ('Enviado', 'Enviado'), ('Entregue', 'Entregue')])

class Avaliacao(models.Model):
    autor = models.ForeignKey(Cliente, on_delete = models.CASCADE, related_name = "avaliacoes")
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE, related_name = "avaliacoes")
    comentario = models.TextField(blank = True, null = True)
    estrelas = models.IntegerField(choices = [(1, '1 estrela'), (2, '2 estrela'), (3, '3 estrela'), (4, '4 estrela'), (5, '5 estrela')])


class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, related_name = "carrinhos")
    produto = models.ManyToManyField(Produto, through = 'ProdutoCarrinho', related_name = "carrinhos")


class Pagamento(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name="pagamento")
    metodo = models.CharField(max_length= 10, choices = [('Cartão', 'Cartão'), ('Boleto', 'Boleto'), ('Pix', 'Pix')])
    data = models.DateTimeField(auto_now_add = True)

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE, related_name = "estoque")
    quantidade = models.PositiveIntegerField()

class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE)
    quantidade = models.PositiveIntegerField()

class ProdutoCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete = models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE)
    quantidade = models.PositiveIntegerField()

