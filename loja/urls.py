from django.urls import path
from . import views
from .views import login_view
from .views import homepage_view
from .views import carrinho_view

urlpatterns = [
    path('', views.principal, name='principal'),
    path('login/', login_view, name='login'),
    path('homepage/', homepage_view, name='homepage'),
     path('adicionar_ao_carrinho/<str:codigo>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', carrinho_view, name='carrinho'),
]