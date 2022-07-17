from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.core.paginator import Paginator


from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

from .forms import *


from .models import *

from genz.models import Profile

from  django.urls import reverse_lazy
"""
The home page contains each category, links to private profile,
"""
class HomePage(TemplateView):
    template_name= 'leak/home.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['leaks'] = Leak.objects.all()[:20]

                    
        # create pagination
        p = Paginator(context['leaks'], 2)
        page = self.request.GET.get('page')
        context['leaks'] = p.get_page(page)


        return context



class LeakDetail(DetailView):
    model = Leak
    context_object_name = 'leak'
    template_name = 'leak/leak_detail.html'
    slug_fields = 'slug'
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leak'].views += 1
        context['leak'].save()

        return context

    def get(self, request, slug):
        return super(LeakDetail, self).get(request, slug)


class CategoryLeakView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'leak/category_leaks.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['category'] # handle like 1000 subcategories
        context['leaks'] = Leak.objects.filter(category=category)[:20]
        context['subcategories'] = Subcategory.objects.filter(category=category)
        context['user'] = self.request.user
        category.views += 1
        category.save()
        return context
        """
        Use algorithm to determine the 10 subcategories that will be displayed on the front page
        
        """
                    
        # create pagination
        p = Paginator(context['leaks'], 2)
        page = self.request.GET.get('page')
        context['leaks'] = p.get_page(page)
        return context

    def get(self, request, slug):
        return super(CategoryLeakView, self).get(request, slug)

"""
Change this get to get context data
"""

class SubcategoryLeakView(TemplateView):
    # model = Subcategory
    # context_object_name = 'subcategory'
    template_name = 'leak/subcategory_leaks.html'



    def get(self, request, slug, *args, **kwargs):
        subcategory = Subcategory.objects.select_related('category').prefetch_related('leaks_subcategory').get(slug=slug)
        category = subcategory.category
        leaks = subcategory.leaks_subcategory.all()
        user = self.request.user
        subcategory.views += 1
        subcategory.save()
        # create pagination
        p = Paginator(leaks, 2)
        print('Working')
        page = self.request.GET.get('page')
        leaks = p.get_page(page)

        context = {
            'subcategory': subcategory,
            'category' : category,
            'leaks' : leaks,
            'user' : user,
        }
        return render(self.request, 'leak/subcategory_leaks.html', context)




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     subcategory = context['subcategory']
    #     context['category'] = subcategory.category
    #     context['leaks'] = Leak.objects.filter(subcategory=subcategory)[:20]
            
    #     # create pagination
    #     p = Paginator(context['leaks'], 2)
    #     print('Working')
    #     page = self.request.GET.get('page')
    #     context['leaks'] = p.get_page(page)

    #     return context



class CategoryCreate(LoginRequiredMixin, CreateView):
    redirect_field_name = 'next'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('leak:home')
    template_name = 'leak/category_create.html'




class SubcategoryCreate(LoginRequiredMixin, FormView):
    redirect_field_name = 'next'
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
            user = self.request.user
            title = form.cleaned_data.get('title')
            slug = form.cleaned_data.get('slug')
            description = form.cleaned_data.get('description')
            category = Category.objects.get(id=category_id)
            try:
                if user.created_subcategory:
                    messages.error(self.request, f"You can't create a country because you've already created one.")
                    return redirect('leak:subcategory-create', category_id=category_id)
            except:
                pass

            # sub = category.subcategories.filter(title__iexact=title)
            # if sub.count() > 0:
            #     messages.error(self.request, f"This country already exists under this continent")
            #     return redirect('leak:subcategory-create', category_id=category_id)


            subcategory = Subcategory.objects.create(title=title, slug=slug, description=description, category=category, creator=user)
            Constitution.objects.create(law=_('Add The Laws Here'), subcategory=subcategory)
            subcategory.members.add(user) # test this later
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

        return redirect('leak:subcategory-leaks', slug=subcategory.slug)







class UpvoteLeak(LoginRequiredMixin, View):
    def get(self, request, leak_id):
        try:
            user = self.request.user
            leak = Leak.objects.prefetch_related('voters').get(id=leak_id)
            if user not in leak.voters.all():
                leak.voters.add(user)
                leak.upvotes += 1
                leak.save()
                upvotes = leak.get_number_of_upvotes
                return HttpResponse(f'{upvotes}')
        except:
            pass
        return HttpResponse('upvoted!')




class DownvoteLeak(LoginRequiredMixin, View):
    def get(self, request, leak_id):
        try:
            user = self.request.user
            leak = Leak.objects.prefetch_related('voters').get(id=leak_id)
            if user not in leak.voters.all():
                leak.voters.add(user)
                leak.downvotes += 1
                leak.save()
                downvotes = leak.get_number_of_downvotes
                return HttpResponse(f'{downvotes}')
        except:
            pass
        return HttpResponse('downvoted!')



"""
Remove category from the subcategory link 
https://www.genbtr.com/leak/Nigeria-politics


add the success url

"""

class ConstitutionEdit(LoginRequiredMixin, UpdateView):
    model = Constitution
    template_name = 'leak/category_create.html'
    form_class = ConstitutionForm
    success_url = reverse_lazy('leak:home')
    redirect_field_name = 'next'


    def form_invalid(self, form):
        messages.error(self.request, f"An Error Occurred!")
        return super().form_invalid(form)

    # def get(self, request, subcategory_id, *args, **kwargs):
    #     """
    #     Add the code check if the person is the president
    #     """
    #     return super(LeakCreate, self).get(request, subcategory_id, *args, **kwargs)



class ConstitutionView(DetailView):
    model = Constitution
    template_name = 'leak/constitution.html'
    context_object_name = 'constitution'



"""
if a user has created a country, the create your own country should be hidden from him or her


"""
class ApplyForCitizenship(LoginRequiredMixin, View):
    redirect_field_name = 'next'
    def get(self, request, slug):
        try:
            user = self.request.user
            subcategory = Subcategory.objects.prefetch_related('members').get(slug=slug)
            subcategory.members.add(user)
            subcategory.likes.add(user)
            if user in subcategory.members.all():
                messages.warning(self.request, _('You are already a citizen of this country'))
                return redirect(self.request.META['HTTP_REFERER'])
            

            """
            Create a page that will inform the user
            """
            messages.success(self.request, _(f"Congratulations! You are now a citizen of ") + str(subcategory))

        except:
            pass 
        """Always return a 404 page"""

        return redirect('leak:subcategory-leaks', slug=slug)



class RenounceCitizenShip(LoginRequiredMixin, View):
    redirect_field_name = 'next'

    def get(self, request, slug):
        try:
            """
            all regulators cannot be removed from members. They must be redirect to resignation page first
            """
            user = self.request.user
            subcategory = Subcategory.objects.prefetch_related('members').get(slug=slug)
            if not user in subcategory.members.all():
                message.warning(self.request, _('You are not a citizen of this country'))
                return redirect(self.request.META['HTTP_REFERER'])

            subcategory.members.remove(user)
            messages.info(self.request, _(f"You are no more a citizen of ") + str(subcategory))

        except:
            pass

        return redirect('genz:profile', username=user.username)




class AddShareCount(View):
    def get(self, request, leak_id):
        leak = Leak.objects.get(id=leak_id)
        leak.shares += 1
        leak.save()
        return HttpResponse('Shared!')


"""
use migrate
"""


class LikeSubcategory(LoginRequiredMixin, View):
    redirect_field_name = 'next'

    def get(self, request, subcategory_id):
        user = self.request.user
        subcategory = Subcategory.objects.prefetch_related('likes').get(id=subcategory_id)
        if not user in subcategory.likes.all():
            subcategory.likes.add(user)
            messages.success(self.request, _("Congratulations, this country has been added to the list of your favorite countries"))
            messages.info(self.request, _("Why not migrate to this country?"))
        else:
            messages.info(self.request, _("You liked this country before"))

        return  redirect('leak:subcategory-leaks', slug=subcategory.slug)





class UnLikeSubcategory(LoginRequiredMixin, View):
    redirect_field_name = 'next'

    def get(self, request, subcategory_id):
        user = self.request.user
        subcategory = Subcategory.objects.prefetch_related('likes').get(id=subcategory_id)
        if user in subcategory.likes.all():
            subcategory.likes.remove(user)
            messages.info(self.request, _("You can add country to favorite whenever you have a change of mind."))

        else:
            messages.info(self.request, _("You country is not in your favorite list"))

        return  redirect('leak:subcategory-leaks', slug=subcategory.slug)


