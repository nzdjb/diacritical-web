from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:term_id>/", views.TermView.as_view(), name="term"),
    path("<int:term_id>/<int:run_id>/", views.run, name="run"),
]
