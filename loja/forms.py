from django import forms
from .models import Cliente, Avaliacao

class ClienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label="Senha")
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Senha")

    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'email', 'telefone', 'dataNasc']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Verifica se as senhas coincidem
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'As senhas não coincidem.')  # Adiciona o erro ao campo 'confirm_password'

        return cleaned_data

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['estrelas', 'comentario']