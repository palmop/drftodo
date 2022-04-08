from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from todo.serializers import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from todo.models import Todo
from todo.pagination import CustomPagination

# CreateAPIViews handle post methods.
class CreateTodoItemAPIView(CreateAPIView):
    
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    # override method perform_create (from mixim create it do a serializer.save())
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
# ListApiView handle get request for list
class ListTodoItemsAPIView(ListAPIView):

    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    #queryset = Todo.objects.all()
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

# ListCreateAPIView handle post and get methods:
class ListCreateTodoItemsAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    # thanks to django_filter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'name', 'description', 'status', 'created_at']
    search_fields = ['id', 'name', 'description', 'status', 'created_at']
    ordering_fields = ['id', 'name', 'description', 'status', 'created_at']
    

    # override method perform_create (from mixim create it do a serializer.save())
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class RetriveUpdateTodoItemAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)