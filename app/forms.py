from django import forms


class ShortURLForm(forms.Form):
    short_url = forms.CharField(label="Paste your Short URL Here:", max_length=50)