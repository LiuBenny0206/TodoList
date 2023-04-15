from django.shortcuts import render
from .models import Todo
from .forms import TodoModelForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
# Create your views here.

class TodoListView(ListView):
    model = Todo
    queryset = Todo.objects.filter(finish=False)
    template_name = 'todo/todo_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TodoModelForm()  #資料模型表單
        return context
class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoModelForm
    success_url = '/todo/'
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoModelForm
    template_name = 'todo/todo_update.html'
    success_url = '/todo/'
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'  # 刪除樣板
    success_url = '/todo'  # 刪除成功後要導向的網址
class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'