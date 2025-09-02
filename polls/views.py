from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Poll, Question, Choice, Vote
from django.contrib.auth.mixins import LoginRequiredMixin

class PollListView(LoginRequiredMixin,View):
    def get(self, request):
        polls = Poll.objects.filter(is_active=True)  
        return render(request, 'poll_list.html', {'polls': polls})


class PollDetailView(LoginRequiredMixin,View): 
    def get(self, request, poll_id, question_number=1):
        poll = get_object_or_404(Poll, id=poll_id, is_active=True)
        questions = poll.questions.all().order_by('id')  

        if question_number > len(questions):
            return redirect('poll_results', poll_id=poll.id)

        question = questions[question_number - 1]
        return render(request, 'poll_detail.html', {
            'poll': poll,
            'question': question,
            'question_number': question_number,
        })
@login_required    
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    votes = Vote.objects.filter(poll=poll, user=request.user)
    return render(request, 'poll_results.html', {'poll': poll, 'votes': votes})

@login_required
def retake_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    Vote.objects.filter(poll=poll, user=request.user).delete()
    return redirect('poll_detail', poll_id=poll_id, question_number=1)