from django.db.models import F
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


# Create your views here.
class QuestionList(ListView):
    template_name = 'home.html'
    queryset = Question.objects.order_by('pub_date')[:5]
    context_object_name = 'questions'


class QuestionDetails(DetailView):
    template_name = 'details.html'
    model = Question
    context_object_name = 'question'


class QuestionResults(DetailView):
    template_name = 'results.html'
    model = Question
    context_object_name = 'question'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return HttpResponse("something went wrong")
    else:
        choice.votes = F('votes') + 1  # prevent race condition
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
