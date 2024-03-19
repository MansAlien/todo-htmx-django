from django.views.generic import TemplateView, ListView
from todo.models import Task

class TodoTemplateView(TemplateView):
    model = Task
    template_name = "home.html"


class TodoListView(ListView):
    model = Task
    template_name = "home.html"
