from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from .models import Test, Question, Choice, Answer
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class TestListView(LoginRequiredMixin, ListView):
    model = Test
    template_name = 'test_list.html'
    context_object_name = 'tests'

class TestCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Test
    template_name = 'test_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('test_list')

    def form_valid(self, form):
        return self.request.user.is_staff

class TakeTestView(LoginRequiredMixin, DetailView):
    model = Test
    template_name = 'take_test.html'
    context_object_name = 'test'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        context['test'] = test
        context['questions'] = self.object.questions.all()
        return context

    def post(self, request, *args, **kwargs):
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        questions = test.questions.all()

        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = get_object_or_404(Choice, id=choice_id)
                Answer.objects.update_or_create(
                    user=request.user,
                    test=test,
                    question=question,
                    defaults={'choice': choice}
                )
        return redirect('test_list')

class TestResultView(LoginRequiredMixin, CreateView):
    model = Answer
    template_name = 'test_result.html'
    context_object_name = 'result'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        answer = Answer.objects.filter(user=self.request.user, test=test).select_related('choice', 'question')
        context['test'] = test
        context['answer'] = answer
        return context