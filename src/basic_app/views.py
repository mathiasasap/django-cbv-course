from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import School, Student


class BasicAppView(TemplateView):
    # template_name = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text"] = "Some context text!"
        return context


class SchoolListView(ListView):
    context_object_name = "schools"  # By default returns in the context school_list (modelname_list)
    model = School


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"  # By default returns in the context school (modelname)
    model = School
    template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    fields = ("name", "principal", "location")
    model = School


class SchoolUpdateView(UpdateView):
    fields = ("name", "principal")
    model = School


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("basic_app:list")