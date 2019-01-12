<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("You're at the add index.")
=======
=======
>>>>>>> 751c87058daf389b97484113501dbb29629abc22
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import Http404, render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Equation, Question

class IndexView(generic.ListView):
    template_name = 'add/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'add/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'add/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.equation_set.get(pk=request.POST['equation'])
    except (KeyError, Equation.DoesNotExist):
        return render(request, 'add/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
<<<<<<< HEAD
        return HttpResponseRedirect(reverse('add:results', args=(question_id,)))
>>>>>>> 751c87058daf389b97484113501dbb29629abc22
=======
        return HttpResponseRedirect(reverse('add:results', args=(question_id,)))
>>>>>>> 751c87058daf389b97484113501dbb29629abc22
