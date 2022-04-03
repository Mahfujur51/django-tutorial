from django.shortcuts import render

from .forms import ContactForm,PostForm
from .models import Contact, Post


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


def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
    else:
        form = PostForm()
    return render(request, 'tuition/postcrate.html', {'form': form})
