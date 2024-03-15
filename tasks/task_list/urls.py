from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from task_list import views


urlpatterns = [
    path('task_list/', views.task_list_list),
    path('task_list/<int:pk>/', views.task_list_detail),
    path('tag/',views.tag_list),
    path('tag/<int:pk>/',views.tag_detail),
    path('all/', views.index, name="index"),
    path('tasks/',views.task_full_list),
    path('tasks/<int:pk>/',views.task_detail)
]


urlpatterns = format_suffix_patterns(urlpatterns)
