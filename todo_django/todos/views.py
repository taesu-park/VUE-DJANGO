from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializers
# Create your views here.

# GET /todos/ : 전체 todos목록 가져오기
# POST /todos/ : todos 등록(저장하기)
@api_view(['GET','POST'])
def todo_index_create(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializers = TodoSerializers(todos, many=True)
        return Response(serializers.data)
    else:
        serializers = TodoSerializers(data=request.POST)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
