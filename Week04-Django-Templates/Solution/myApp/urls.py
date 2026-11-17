from django.urls import path
from . import views
app_name = 'myApp'
urlpatterns = [
    path('', views.home, name='home'),
    path('students/<int:page>/', views.studentlist, name='studentlist'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('modules/', views.modulelist, name='modulelist'),
]
