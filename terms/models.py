from django.db import models


class Term(models.Model):
    term = models.CharField(max_length=50)

    def __str__(self):
        return self.term


class Run(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return str(self.pk)


class Finding(models.Model):
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    url = models.TextField()
    page_name = models.TextField()

    def __str__(self):
        return self.page_name
