from rest_framework.serializers import ModelSerializer
from drf_extra_fields.fields import Base64ImageField

from todo.models import Todo

class TodoSerializer(ModelSerializer):
    image = Base64ImageField()
    class Meta:
        model = Todo
        fields = ['id', 'name', 'description', 'deadline', 'created_at', 'status', 'image']

