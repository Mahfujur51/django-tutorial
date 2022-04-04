from statistics import mode

from django import forms

from .models import Contact, Post


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactFormtwo(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    # name = forms.CharField(label='Name', max_length=100)
    # phone = forms.CharField(label='Phone', max_length=100)
    # content = forms.CharField(label='Your Details', max_length=100)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'id', 'created_at', 'slug', ]
        widgets = {
            'class_in': forms.CheckboxSelectMultiple(attrs={
                'multiple': True
            }),
            'subject': forms.CheckboxSelectMultiple(attrs={
                'multiple': True
            }),

        }
