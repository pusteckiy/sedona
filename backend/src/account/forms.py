from django import forms
from django.core.validators import validate_ipv46_address


class ConnectAccountForm(forms.Form):
    nickname = forms.CharField(
        label='Укажите свой никнейм.', 
        max_length=38, 
        min_length=3, 
        widget=forms.TextInput(
            attrs={'class': 'input-form', 'placeholder': 'Никнейм'}
            )
        )


class InputAccountCodeForm(forms.Form):
    code = forms.CharField(
        label='Введите код подтверждения.', 
        max_length=6, 
        min_length=6,
        widget=forms.TextInput(
            attrs={'class': 'input-form', 'placeholder': 'Код подтверждения'}
            )
        )


class ClearAccountFromRakBotForm(forms.Form):
    ip = forms.GenericIPAddressField(protocol='IPv4', 
                                     validators=[validate_ipv46_address], 
                                     widget=forms.TextInput(attrs={'class': 'input-form', 'placeholder': 'Введите свой IPv4 адрес', 'id': 'ip-field'}))
