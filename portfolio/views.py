from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from portfolio.forms import ProjectForm
from .models import Project, ProjectImage


# 🔹 Список усіх проектів
class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/project_list.html"
    context_object_name = "projects"
    ordering = ["-created_at"]


# 🔹 Детальний перегляд одного проекту
class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"


# 🔹 Створення проекту (тільки авторизованим)
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "portfolio/project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy('project-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        images = form.cleaned_data.get('images')
        if images:
            for image in images:
                ProjectImage.objects.create(project=self.object, image=image)
        return response


# 🔹 Редагування проекту (тільки автор)
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "portfolio/project_form.html"
    success_url = reverse_lazy("project-list")
    

    def form_valid(self, form):
        response = super().form_valid(form)
        images = form.cleaned_data.get('images')
        if images:
            for image in images:
                ProjectImage.objects.create(project=self.object, image=image)
        return response

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.user


# 🔹 Видалення проекту (тільки автор)
class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "portfolio/project_confirm_delete.html"
    success_url = reverse_lazy("project-list")

    def test_func(self):
        project = self.get_object()
        return self.request.user == project.user
