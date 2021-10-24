from django import forms


class contractFroms(forms.Form):
    name = forms.CharField( max_length= 20, label="your name")
    phone = forms.CharField( max_length= 20, label="your name")
    content = forms.CharField( max_length= 20, label="your name")