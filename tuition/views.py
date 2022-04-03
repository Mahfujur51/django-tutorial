from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm, PostForm
from .models import Contact, Post, Subject


# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # phone = form.cleaned_data['phone']
            # content = form.cleaned_data['content']
            # obj = Contact(name=name, phone=phone, content=content)
            # obj.save()
        # return HttpResponse("<h1>Thanks for contacting us</h1>")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def postview(request):
    post = Post.objects.all()
    return render(request, 'tuition/postview.html', {'post': post})


def subjectview(request):
    subject = Subject.objects.get(name="Physics")
    post = subject.subject_set.all()

    return render(request, 'tuition/subject/subjectview.html', {'subject': subject, 'post': post})


def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            sub = form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in = form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse("Data Save Successfully!!")
    else:
        form = PostForm()
    return render(request, 'tuition/postcrate.html', {'form': form})
