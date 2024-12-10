from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    es_admin = forms.BooleanField(required=False, label="¿Hacer administrador?", help_text="Selecciona esta opción para otorgar privilegios de administrador.")
    phone = forms.CharField(max_length=15, label='Número de teléfono', required=False)  # Campo personalizado
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data
