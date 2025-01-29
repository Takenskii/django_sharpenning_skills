from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=1000)


