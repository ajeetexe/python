from django.urls import path
from . import views



urlpatterns=[
    path('',views.IndexManagementView.as_view(),name='management_home'),
]