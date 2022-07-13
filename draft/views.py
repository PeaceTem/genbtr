from django.shortcuts import render, redirect


# function based views
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from django.views import View
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import DraftLeak
from leak.models import Subcategory, Leak, Category


from leak.forms import LeakForm

from .forms import DraftLeakForm
# Create your views here.


class DraftLeakCreate(LoginRequiredMixin, View):
    def get(self, request, category_id, subcategory_id):
        form = LeakForm()
        context = {
            'form' : form,
            
        }
        return render(self.request, 'leak/leak_create.html', context)


    def post(self, request, category_id, subcategory_id):
        form = DraftLeakForm(self.request.POST)
        if form.is_valid():
            user = self.request.user
            title = form.cleaned_data.get('title')
            story = form.cleaned_data.get('story')
            category = Category.objects.get(id=category_id)
            subcategory = Subcategory.objects.get(id=subcategory_id)
            draft = DraftLeak.objects.create(user=user, title=title, story=story, category=category, subcategory=subcategory)

            return redirect('draft:leak-draft-list')

        # return a error message





# class DraftLeakCreate(LoginRequiredMixin, FormView):
#     model = DraftLeak
#     template_name= 'leak/leak_create.html'
#     success_url = reverse_lazy('leak:home')
#     form_class = DraftLeakForm



#     def form_valid(self, form, category_id, subcategory_id):
#         form.instance.user = self.request.user
#         form.instance.category = Category.objects.get(id=category_id)
#         form.instance.subcategory = Subcategory.objects.get(id=subcategory_id)
#         form.save()

#         return super(DraftLeakCreate, self).form_valid(form)

#     def get(self, request, category_id, subcategory_id):
#         form = DraftLeakForm()
#         context = {
#             'form' : form,
            
#         }
#         return render(self.request, 'leak/leak_create.html', context)




"""
header

back   GenBTR    menu

"""



class DraftLeakUpdate(LoginRequiredMixin, UpdateView):
    model = DraftLeak
    template_name='leak/leak_create.html'
    # fields = ('title', 'story')
    form_class = DraftLeakForm
    success_url = reverse_lazy('draft:leak-draft-list')






class DraftLeakList(LoginRequiredMixin, ListView):
    
    model = DraftLeak
    template_name= 'draft/leak_list.html'
    context_object_name = 'leaks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leaks'] = context['leaks'].filter(user=self.request.user)
        return context



class DraftLeakDetail(LoginRequiredMixin, DetailView):
    model = DraftLeak
    template_name= 'draft/leak_detail.html'
    context_object_name = 'draft'




class DraftLeakDelete(LoginRequiredMixin, View):

    def get(self, request, pk):
        draft = DraftLeak.objects.get(id=pk)
        draft.delete()
        return redirect('draft:leak-draft-list')





class ConvertDraftToLeak(LoginRequiredMixin, View):
    def get(self, request, draft_id):
        draft = DraftLeak.objects.get(id=draft_id)
        try:
            leak = Leak.objects.create(title=draft.title, story=draft.story, category=draft.category, subcategory=draft.subcategory)
            draft.delete()
        except:
            return redirect(self.request.META['HTTP_REFERER'])

        return redirect('leak:leak-detail', pk=leak.id)





