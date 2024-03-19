from django.urls import path
from todo.views import TodoTemplateView, TodoListView

urlpatterns = [
    path("", TodoTemplateView.as_view(), name="home" ),
    path("list/", TodoListView.as_view(), name="list"),
]
