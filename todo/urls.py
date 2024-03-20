from django.urls import path
from todo.views import TodoListView, createview, renameview, cancelview, applyview, deleteview

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
    path("create/", createview, name="create"),
    path("<int:pk>/rename/", renameview, name="rename"),
    path("cancel/", cancelview, name="cancel"),
    path("<int:pk>/apply/", applyview, name="apply"),
    path("<int:pk>/delete/", deleteview, name="delete"),
]
