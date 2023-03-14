from django import forms


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