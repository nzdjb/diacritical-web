from django.shortcuts import render

from .models import Term


def index(request):
    context = {
        "term_list": Term.objects.all()
    }
    return render(request, 'terms/index.html', context)
