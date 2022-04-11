from statistics import mode

from django import forms

from .models import Contact, Post


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    def __init__(self,*args,**keyargs):
        super().__init__(*args,**keyargs)
        self.fields['name'].label="My Name"
        self.fields['name'].initial="Mahfujur Rahman"


        self.fields['phone'].label="Your Phone Number:"
        self.fields['phone'].initial="+8801"


        self.fields['content'].label="Message"
        self.fields['content'].initial="Mahfujur Rahman"

    def clean_name(self):
        value = self.cleaned_data.get('name')
        num_of_words =value.split(' ')
        if len(num_of_words)>3:
            self.add_error('name','Name can have maximum of  3words')
        else:
            return value


        # for field in self.fields:
        #     self.fields[field].widget.attrs.update({'class':'form-control'})

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please Say something','rows':5}),
        # }
        # labels={
        #     'name': 'Your Name',
        #     'phone': 'Phone Number',
        #     'content': 'Message',
        # }
        # help_texts={
        #     'name': 'Please enter your name',
        #     'phone': 'Please enter your phone number',
        #     'content': 'Please enter your message',
        # }


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
