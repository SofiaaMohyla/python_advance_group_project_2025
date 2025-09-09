from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from .models import Test, Question, Choice, Answer
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class TestListView(LoginRequiredMixin, ListView):
    model = Test
    template_name = 'test/test_list.html'
    context_object_name = 'tests'


class TestCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Test
    template_name = 'test/test_create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('test/test_list')

    def test_func(self):
        return self.request.user.is_staff
    
    def get_success_url(self):
        return reverse('question_create', kwargs={'test_id': self.object.id})
    

class QuestionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Question
    fields = ['text']
    template_name = 'test/question_form.html'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        test = get_object_or_404(Test, id=self.kwargs['test_id'])
        form.instance.test = test
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('choice_create', kwargs={'question_id': self.object.id})
    

class ChoiceCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Choice
    fields = ['text', 'is_correct', 'img']
    template_name = 'test/choice_form.html'

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        question = get_object_or_404(Question, id=self.kwargs['question_id'])
        form.instance.question = question
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('choice_create', kwargs={'question_id': self.object.question.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = get_object_or_404(Question, id=self.kwargs['question_id'])
        choices = question.choices.all()

        context['question'] = question
        context['choices'] = choices
        # 👉 логіка винесена з шаблону
        context['enough_choices'] = choices.count() >= 2
        context['has_correct'] = choices.filter(is_correct=True).exists()
        return context


class TakeTestView(LoginRequiredMixin, DetailView):
    model = Test
    template_name = 'test/take_test.html'
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

def take_test(request, pk, question_id):
    test = get_object_or_404(Test, pk=pk)
    question = get_object_or_404(Question, pk=question_id)
    
    total_questions = test.questions.count()
    user_answers = Answer.objects.filter(user=request.user, test=test).count()
    if user_answers == total_questions and total_questions > 0:
        return redirect('test/test_result', pk=test.id)

    if request.method == 'POST':
        choice_id = request.POST.get(f'question_{question.id}')
        if choice_id:
            choice = get_object_or_404(Choice, id=choice_id)
            Answer.objects.create(
                user=request.user,
                test=test,
                question=question,
                choice=choice,
            )
        next_question = test.questions.filter(id__gt=question.id).first()
        if next_question:
            return redirect('test/take_test', pk=test.id, question_id=next_question.id)
        else:
            return redirect('test/test_result', pk=test.id)

    context = {
        'test': test,
        'question': question
    }
    return render(request, 'test/take_test.html', context)



class TestResultView(LoginRequiredMixin, DetailView):
    model = Answer
    template_name = 'test/test_result.html'
    context_object_name = 'result'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = get_object_or_404(Test, pk=self.kwargs['pk'])
        answer = Answer.objects.filter(user=self.request.user, test=test).select_related('choice', 'question')
        score = sum(1 for a in answer if  a.choice.is_correct)
        context['test'] = test
        context['answer'] = answer
        context['score'] = score
        return context