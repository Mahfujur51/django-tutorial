

# from django.http import HttpResponse
from unicodedata import name

from django.shortcuts import HttpResponse, render

# from tuition.models import Contact


def home(reqeuest):
    name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    context = {
        "name": name
    }
    return render(reqeuest, 'home.html', context)


# def contact(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         phone = request.POST['phone']
#         content = request.POST['content']
#         contact = Contact(name=name, phone=phone, content=content)
#         contact.save()
#         # return HttpResponse("<h1>Thanks for contacting us</h1>")
#     return render(request, 'contact.html')
