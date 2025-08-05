from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Poll, Question, Choice, Vote

@method_decorator(login_required, name='dispatch')
class PollListView(View):
    def get(self, request):
        polls = Poll.objects.filter(is_active=True)
        return render(request, 'polls/poll_list.html', {'polls': polls})

@method_decorator(login_required, name='dispatch')
class PollDetailView(View):
    def get(self, request, poll_id, question_number=1):
        poll = get_object_or_404(Poll, id=poll_id, is_active=True)
        questions = poll.question_set.all().order_by('id')
        
        if question_number > len(questions):
            return redirect('poll_results', poll_id=poll.id)
            
        question = questions[question_number - 1]
        return render(request, 'polls/poll_detail.html', {
            'poll': poll,
            'question': question,
            'question_number': question_number,
        })

    def post(self, request, poll_id, question_number):
        poll = get_object_or_404(Poll, id=poll_id, is_active=True)
        choice_id = request.POST.get('choice')
        
        if choice_id:
            choice = get_object_or_404(Choice, id=choice_id)
            Vote.objects.create(
                user=request.user,
                poll=poll,
                question=choice.question,
                choice=choice
            )
            
            next_question = question_number + 1
            questions_count = poll.question_set.count()
            
            if next_question > questions_count:
                return redirect('poll_results', poll_id=poll.id)
            else:
                return redirect('poll_detail', poll_id=poll.id, question_number=next_question)
        
        return redirect('poll_detail', poll_id=poll.id, question_number=question_number)