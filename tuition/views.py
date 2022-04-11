from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)
from pyexpat import model

from .forms import ContactForm, PostForm
from .models import Contact, Post, Subject


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    # success_url='/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('contact')
# class ContactView(View):
#     form_class = ContactForm
#     template_name = 'contact.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             contact = form.save(commit=False)
#             contact.save()
#             return HttpResponse('Thank you for your message.')
#         return render(request, self.template_name, {'form': form})


# Create your views here.
# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # name = form.cleaned_data['name']
#             # phone = form.cleaned_data['phone']
#             # content = form.cleaned_data['content']
#             # obj = Contact(name=name, phone=phone, content=content)
#             # obj.save()
#         # return HttpResponse("<h1>Thanks for contacting us</h1>")
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})


def postview(request):
    post = Post.objects.all()
    return render(request, 'tuition/postview.html', {'post': post})


class PostListView(ListView):
    template_name = 'tuition/postlist.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = context.get('object_list')
        context['msg'] = "This is post list"
        return context

    # model = Post

    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = context.get('object_list')
        context['msg'] = "This is post list"
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'tuition/postdetails.html'


def subjectview(request):
    subject = Subject.objects.get(name="Physics")
    post = subject.subject_set.all()

    return render(request, 'tuition/subject/subjectview.html', {'subject': subject, 'post': post})


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'tuition/postcrate.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    # def get_success_url(self):
    #     # id = self.object.id
    #     return reverse_lazy('tuition:subject')
    #     # return super()().get_success_url()


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'tuition/postcrate.html'

    def get_success_url(self):
        id = self.object.id
        return reverse_lazy('tuition:postdetails', kwargs={'pk': id})


# def postcreate(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             sub = form.cleaned_data['subject']
#             for i in sub:
#                 obj.subject.add(i)
#                 obj.save()
#             class_in = form.cleaned_data['class_in']
#             for i in class_in:
#                 obj.class_in.add(i)
#                 obj.save()
#             return HttpResponse("Data Save Successfully!!")
#     else:
#         form = PostForm()
#     return render(request, 'tuition/postcrate.html', {'form': form})

class PostDeleteView(DeleteView):
    model=Post
    template_name = 'tuition/postdelete.html'
    success_url = reverse_lazy('tuition:postlist')
