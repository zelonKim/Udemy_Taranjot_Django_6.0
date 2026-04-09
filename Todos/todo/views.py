from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import TodoForm
from .models import Todos
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView



# class HomeView(View):
#     def get(self, request):
#         todos = Todos.objects.all()
#         return render(request, "todo/index.html", {'todos':todos})
    
    
    
class HomeView(ListView):
    model = Todos
    ordering = ['-id']
    template_name = 'todo/index.html'
    context_object_name = 'todos'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['name'] = 'rahul'
    #     return context
    
    # def get_queryset(self):
    #     return Todos.objects.filter(todo__icontains='market')
    
    
    
##################################


class DetailTodoView(DetailView):
    model = Todos
    template_name = 'todo/detail.html'
    context_object_name = 'todo'
    
    

##################################


    
# class AddView(View):
#     def get(self, request):
#         form = TodoForm()
#         return render(request, 'todo/add.html', {'form':form})
    
#     def post(self, request):
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#         return



# class AddView(FormView):
#     template_name = 'todo/add.html'
#     form_class = TodoForm
#     success_url = '/'
    
#     def form_valid(self, form):
#         print(form.cleaned_data['todo'])
#         form.save()
#         return super().form_valid(form)



class AddView(CreateView):
    model = Todos
    # fields = '__all__'
    success_url = '/'
    # template_name = 'todo/add.html'
    template_name_suffix = '_add'
    form_class = TodoForm




##################################



class UpdateTodoView(UpdateView):
    model = Todos
    fields = "__all__"
    success_url = '/'
    

##################################



class DeleteTodoView(DeleteView):
    model = Todos
    success_url = '/'


##################################


class AboutView(TemplateView):
    template_name = 'todo/about.html'
    
    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['CompanyName'] = 'Taranjot Sing'
        return context
    
    
##################################



class RedirectAbout(RedirectView):
   pattern_name = 'home'
   query_string = True
   
   
