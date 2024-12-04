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

class PedidoProdutoInline(admin.TabularInline):
    model = PedidoProduto

class PedidoAdmin(admin.ModelAdmin):
    model = Pedido
    inlines = [PedidoProdutoInline,]
    list_display = ("cliente", "valor", "status")

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("autor", "pedido")

class ProdutoCarrinhoInline(admin.TabularInline):
    model = ProdutoCarrinho

class CarrinhoAdmin(admin.ModelAdmin):
    model = Carrinho
    inlines = [ProdutoCarrinhoInline,]
    list_display = ("cliente",)

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "metodo", "data")

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade")

#class PedidoProdutoAdmin(admin.ModelAdmin):
 #   list_display = ("pedido", "produto", "quantidade")


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Avaliacao, AvaliacaoAdmin)
admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Estoque, EstoqueAdmin)
#admin.site.register(PedidoProduto, PedidoProdutoAdmin)

#login e senha: admin