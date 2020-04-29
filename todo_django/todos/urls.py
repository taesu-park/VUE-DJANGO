from django.urls import path

urlpatterns = [
    path('todos/', views.todo_index_create)
]