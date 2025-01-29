from django.urls import path
from .views import login_view,homepage_view, adicionar_ao_carrinho, carrinho_view, cadastro_view, diminuir_quantidade, aumentar_quantidade, remover_do_carrinho, finalizar_compra, sair, pedido_sucesso

urlpatterns = [
    path('', login_view, name='login'),
    path('homepage/', homepage_view, name='homepage'),
    path('adicionar_ao_carrinho/<str:codigo>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', carrinho_view, name='carrinho'),
    path('sair/', sair, name='sair'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('carrinho/diminuir/<str:codigo>/', diminuir_quantidade, name='diminuir_quantidade'),
    path('carrinho/aumentar/<str:codigo>/', aumentar_quantidade, name='aumentar_quantidade'),
    path('carrinho/remover_do_carrinho/<str:codigo>/', remover_do_carrinho, name='remover_do_carrinho'),
    path('finalizar_compra/', finalizar_compra, name='finalizar_compra'),
    path('pedido-sucesso/<int:pedido_id>/', pedido_sucesso, name='pedido_sucesso'),
]   