from django.shortcuts import render
from django.views.generic import ListView
from .models import Course

class CourseListView(ListView): # get.objects.all()
    model = Course
    template_name = "school/course_list.html"
    context_object_name = "courses"


# class 