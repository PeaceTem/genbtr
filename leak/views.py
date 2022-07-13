from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import *


from .models import *



from  django.urls import reverse_lazy
"""
The home page contains each category, links to private profile,
"""
class HomePage(TemplateView):
    template_name= 'leak/home.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['leaks'] = Leak.objects.filter(votes__gte=0)[:20]
        return context



class LeakDetail(DetailView):
    model = Leak
    context_object_name = 'leak'
    template_name = 'leak/leak_detail.html'



class CategoryLeakView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'leak/category_leaks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['category']
        context['leaks'] = Leak.objects.filter(category=category)[:10]
        context['subcategories'] = Subcategory.objects.filter(category=category)
        return context




class SubcategoryLeakView(DetailView):
    model = Subcategory
    context_object_name = 'subcategory'
    template_name = 'leak/subcategory_leaks.html'



    def get(self, request, category_id, pk, *args, **kwargs):

        return super(SubcategoryLeakView, self).get(request, category_id, pk, *args, **kwargs)




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategory = context['subcategory']
        context['category'] = subcategory.category
        context['leaks'] = Leak.objects.filter(subcategory=subcategory)[:20]
        return context



class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('leak:home')
    template_name = 'leak/category_create.html'




class SubcategoryCreate(LoginRequiredMixin, FormView):
    model = Subcategory
    form_class = SubcategoryForm
    success_url = reverse_lazy('leak:home')
    template_name = 'leak/category_create.html'


    def get(self, request, category_id, *args, **kwargs):

        return super(SubcategoryCreate, self).get(request, category_id, *args, **kwargs)




    def form_invalid(self, form):
        messages.error(self.request, f"An Error Occurred!")
        return super().form_invalid(form)



    def post(self, request, category_id, *args, **kwargs):
        form = SubcategoryForm(self.request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            category = Category.objects.get(id=category_id)
            subcategory = Subcategory.objects.create(title=title, description=description, category=category)

        return redirect('leak:subcategory-leaks', category_id=category.id, pk=subcategory.id)





class LeakCreate(FormView):
    template_name= 'leak/leak_create.html'
    form_class = LeakForm



    def form_invalid(self, form):
        messages.error(self.request, f"An Error Occurred!")
        return super().form_invalid(form)


    def get(self, request, category_id, subcategory_id, *args, **kwargs):

        return super(LeakCreate, self).get(request, category_id, subcategory_id, *args, **kwargs)


    def post(self, request, category_id, subcategory_id, *args, **kwargs):
        form = LeakForm(self.request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            story = form.cleaned_data.get('story')
            category = Category.objects.get(id=category_id)
            subcategory = Subcategory.objects.get(id=subcategory_id)
            leak = Leak.objects.create(title=title, story=story, category=category, subcategory=subcategory)

        return redirect('leak:subcategory-leaks', category_id=category.id, pk=subcategory_id)







