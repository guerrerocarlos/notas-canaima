from django import forms
from captcha.fields import CaptchaField


class formulario_principal(forms.Form):
	codigo_form = forms.CharField(widget=forms.Textarea,label='')
	titulo_form = forms.CharField(required=False, label='Titulo')
	nombre_form = forms.CharField(required=False, label='Autor')
	captcha = CaptchaField(label='Captcha')


