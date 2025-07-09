from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from django.contrib import admin

from .views import(
	CustomLoginView,
	group_check,
	logout_view,
	register_teacher,
	register_student,
	)

urlpatterns = [
      path('', CustomLoginView.as_view(template_name='index.html'), name="home"),
      path('logout/', views.logout_view, name='logout'),
      path('group/', views.group_check, name='group'),
      path('register_teacher/', views.register_teacher, name='register_teacher'),
      path('register_student/', views.register_student, name='register_student'),
]