from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Course
from django.urls import reverse_lazy

class CourseListView(ListView): # get.objects.all()
    model = Course
    template_name = "school/course_list.html"
    context_object_name = "courses"


class CourseDetailView(DetailView):   
    model = Course
    template_name = "school/course_detail.html"
    context_object_name = "course"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.object.students.all()
        return context
    

class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'description']
    template_name = "school/course_form.html"
    success_url = reverse_lazy("course-list")


    


