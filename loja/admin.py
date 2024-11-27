from django.contrib import admin
from .models import Cliente
from .models import Produto
from .models import Pedido
from .models import Avaliacao
from .models import Carrinho
from .models import Pagamento
from .models import Estoque
from .models import PedidoProduto
from .models import ProdutoCarrinho

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ["nome"]

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo", "preco")
    search_fields = ["nome", "codigo"]

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "valor", "status")

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("autor", "pedido")

#carrinho não está atualizando, verificar
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ("cliente", Produto)

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "metodo", "data")

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade")

class PedidoProdutoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade")

class ProdutoCarrinhoAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade")


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(PedidoProduto, PedidoProdutoAdmin)
admin.site.register(ProdutoCarrinho, ProdutoCarrinhoAdmin)

#login e senha: admin