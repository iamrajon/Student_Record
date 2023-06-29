from django.urls import path 
from core import views

urlpatterns = [
    path('', views.student_view, name="create-student"),
    path('delete_student/<int:id>/', views.delete_student, name="delete-student"),
    path('update_student/<int:id>/', views.edit_student, name="update-student"),
]
