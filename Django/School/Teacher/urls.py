from django.urls import path
from . import views


urlpatterns=[
    path('',views.TeacherView.as_view(),name='teacher_home'),
]