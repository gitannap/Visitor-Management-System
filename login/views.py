from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import path
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib import messages

class CustomLoginView(LoginView): 
    def form_valid(self, form):
        # Perform the default action first
        response = super().form_valid(form)

        # Check if the user is authenticated
        if self.request.user.is_authenticated:
            # User is authenticated, no need to check further
            return response

        return response

    def form_invalid(self, form):
        # Password is incorrect, print a message
        print("Invalid username or password.")
        messages.error(self.request, "Invalid username or password.")

        # Call parent class's form_invalid method to handle the response
        return super().form_invalid(form)


def group_check(request):
    group_name=Group.objects.all().filter(user = request.user)# get logget user grouped name
    group_name=(str(group_name[0]) if group_name else '') # convert to string
    if "Student" == group_name:
         return redirect('student_home')
    elif "Teacher" == group_name:
         return redirect('teacher_home')
    
    elif request.user.username in ['administrator', 'admin']:
         return redirect('admin:index')

def logout_view(request):
	logout(request)
	return redirect('home')


def register_teacher(request):
    return render(request, 'register_teacher.html')

def register_student(request):
    return render(request, 'register_student.html')

