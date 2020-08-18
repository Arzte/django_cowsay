from django import forms


class CowsayForm(forms.Form):
    cowsayify = forms.CharField(max_length=80)
