from django.contrib import admin

from .models import Finding, Run, Term

admin.site.register(Term)
admin.site.register(Run)
admin.site.register(Finding)
