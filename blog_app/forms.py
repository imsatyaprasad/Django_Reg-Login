from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Enter your name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your First Name'}))
    last_name = forms.CharField(label='Enter your Last Name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Last Name'}))
    mobile = forms.IntegerField(label='Enter your Mobile Number',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'your mobile number'}))
    email = forms.EmailField(label='Enter your Email ID',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'your email id'}))
    username = forms.CharField(label='Enter username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your username'}))
    password1 = forms.CharField(label='Enter password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2 = forms.CharField(label='Enter confirmation password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter confirmation password'}))

class LoginForm(forms.Form):
    username = forms.CharField(label='Enter username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your username'}))
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter password'}))