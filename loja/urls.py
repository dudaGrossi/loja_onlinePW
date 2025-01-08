from django.urls import path
from . import views
from .views import login_view,homepage_view, carrinho_view, cadastro_view

urlpatterns = [
    path('', login_view, name='login'),
    path('homepage/', homepage_view, name='homepage'),
    path('adicionar_ao_carrinho/<str:codigo>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', carrinho_view, name='carrinho'),
    path('cadastro/', cadastro_view, name='cadastro'),
]