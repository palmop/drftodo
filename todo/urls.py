from django.urls import path
from todo import views

urlpatterns = [
    path('', views.ListCreateTodoItemsAPIView.as_view(), name="todo-list-create"),
    path('<int:id>', views.RetriveUpdateTodoItemAPIView.as_view(), name="todo-retrive-update"),
    # path('list', views.ListTodoItemsAPIView.as_view(), name="todo-list"),
    # path('create', views.CreateTodoItemAPIView.as_view(), name="todo-create"),
]