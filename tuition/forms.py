from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
    content = forms.CharField(label='Your Details', max_length=100)
