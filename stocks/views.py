
from django.shortcuts import render

from todo.models import ToDo


def index(request):
    todo = ToDo.objects.filter(done=False)
    return render(request, "index.html", {'todo': todo})
