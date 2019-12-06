from django.urls import path
from . import views



urlpatterns=[
    path('',views.IndexStudentView.as_view(),name='student_home'),
    path('studentregister/',views.RegisterstudentView.as_view(),name='studentregister'),
]