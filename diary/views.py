from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Lesson, Grade
from .forms import LessonForm, GradeForm

def lesson_list(request):
    lessons = Lesson.objects.all().order_by('-date')
    return render(request, 'diary/lesson_list.html', {'lessons': lessons})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    grades = Grade.objects.filter(lesson=lesson)
    return render(request, 'diary/lesson_detail.html', {'lesson': lesson, 'grades': grades})

def grade_create(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.lesson = lesson
            grade.save()
            return redirect('lesson_detail', pk=lesson.id)
    else:
        form = GradeForm()
    return render(request, 'diary/grade_form.html', {'form': form, 'lesson': lesson})

class LessonListView(ListView):
    model = Lesson
    template_name = 'diary/lesson_list.html'
    context_object_name = 'lessons'
    ordering = ['-date']

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'diary/lesson_detail.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grades'] = Grade.objects.filter(lesson=self.object)
        return context

class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'diary/lesson_form.html'
    success_url = reverse_lazy('lesson_list')

class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'diary/lesson_form.html'
    success_url = reverse_lazy('lesson_list')

class GradeCreateView(CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'diary/grade_form.html'

    def form_valid(self, form):
        lesson = get_object_or_404(Lesson, pk=self.kwargs['lesson_id'])
        form.instance.lesson = lesson
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('lesson_detail', kwargs={'pk': self.kwargs['lesson_id']})

class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'diary/lesson_confirm_delete.html'
    success_url = reverse_lazy('lesson_list')

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'diary/grade_confirm_delete.html'
    success_url = reverse_lazy("grade_list")

@login_required
def grade_create(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.student = request.user
            grade.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'diary/grade_form.html', {'form': form})

@login_required
def grade_list(request):
    if request.user.is_superuser or request.user.role == "admin":
        grades = Grade.objects.all()
    else:
        grades = Grade.objects.filter(student=request.user)

    return render(request, "diary/grade_list.html", {"grades": grades})


def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect("grade_list")
    else:
        form = GradeForm(instance=grade)
    return render(request, "diary/grade_edit.html", {"form": form, "title": "Редагувати оцінку"})