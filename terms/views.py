from django.utils import timezone
from django.shortcuts import render
from django.views import View

from .models import Finding, Run, Term


def index(request):
    context = {"term_list": Term.objects.all()}
    return render(request, "terms/index.html", context)


class TermView(View):
    def get(self, request, term_id):
        context = {
            "term": Term.objects.get(pk=term_id),
            "run_list": Run.objects.filter(term=term_id),
        }
        return render(request, "terms/term.html", context)

    def post(self, request, term_id):
        Run(term_id=term_id).save()
        return self.get(request, term_id)


def run(request, term_id, run_id):
    context = {
        "term": Term.objects.get(pk=term_id),
        "run": Run.objects.get(pk=run_id),
        "finding_list": Finding.objects.filter(run=run_id),
    }
    return render(request, "terms/run.html", context)
