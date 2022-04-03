from django.shortcuts import render

from .forms import ContactForm
from .models import Contact


# Create your views here.
def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        name = request.POST['name']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name, phone=phone, content=content)
        contact.save()
        # return HttpResponse("<h1>Thanks for contacting us</h1>")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
