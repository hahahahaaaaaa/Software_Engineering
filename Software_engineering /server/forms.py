from django import forms

from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)

class ForgetPasswordForm(forms.Form):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': '用户名'}))
    question = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': '密保问题'}))
    answer = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': '密保答案'}))
    password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={'placeholder': '要重置的密码'}))