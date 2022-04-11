# from multiprocessing import context
# from unittest import result

from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)
from pyexpat import model

from .forms import ContactForm, PostForm
from .models import Class_in, Contact, Post, Subject


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    # success_url='/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thanks for contacting us')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('tuition:contact')
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
def contact(request):
    initials = {
        'name': 'My Name is ',
        'phone': '+8801',
        'content': 'My problem is ',
    }
    if request.method == "POST":
        form = ContactForm(request.POST, initial=initials)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # phone = form.cleaned_data['phone']
            # content = form.cleaned_data['content']
            # obj = Contact(name=name, phone=phone, content=content)
            # obj.save()
        # return HttpResponse("<h1>Thanks for contacting us</h1>")
    else:
        form = ContactForm(initial=initials)
    return render(request, 'contact.html', {'form': form})


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
        context['subjects'] = Subject.objects.all()
        context['classes'] = Class_in.objects.all()
        return context

    # model = Post

    # context_object_name = "posts"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["posts"] = context.get('object_list')
    #     context['msg'] = "This is post list"
    #     return context


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
    model = Post
    template_name = 'tuition/postdelete.html'
    success_url = reverse_lazy('tuition:postlist')


def search(request):
    query = request.POST.get('search', '')
    if query:
        queryset = (Q(title__icontains=query)) | (Q(details__contains=query)) | (
            Q(medium__icontains=query)) | (Q(salary__icontains=query)) | (Q(subject__name__icontains=query)) | (Q(class_in__name__icontains=query))
        results = Post.objects.filter(queryset).distinct()
    else:
        results = []
    context = {
        'results': results,
    }
    return render(request, 'tuition/search.html', context)


def filter(request):
    if request.method == "POST":
        subject = request.POST.get('subject', '')
        class_in = request.POST.get('class_in', '')
        availabe = request.POST.get('availabe', '')
        salary_from = request.POST.get('salary_from', '')
        salary_to = request.POST.get('salary_to', '')
        if subject or class_in:
            queryset = (Q(subject__name__icontains=subject)) & (
                Q(class_in__name__icontains=class_in))
            results = Post.objects.filter(queryset).distinct()
            if availabe:
                results = results.filter(availabe=True)
            if salary_from:
                results = results.filter(salary__gte=salary_from)
            if salary_to:
                results = results.filter(salary__lte=salary_to)

        else:
            results = []
        context = {
            'results': results
        }
        return render(request, 'tuition/search.html', context)
