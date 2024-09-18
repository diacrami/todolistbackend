from django.urls import path
from .views import (TasksListView,
     TasksCreateView,
     TasksUpdateView, 
     TasksDetailView,
     TaskFilterView
    )

urlpatterns = [
    path('listtask', TasksListView.as_view()),
    path('createtask', TasksCreateView.as_view()),
    path('updatetask/<int:pk>', TasksUpdateView.as_view()),
    path('detailtask/<int:pk>', TasksDetailView.as_view()),
    path('filter/<str:tasks>', TaskFilterView.as_view())

]