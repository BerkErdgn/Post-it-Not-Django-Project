from django.db import models

# Create your models here.

class AddNot(models.Model):
    author = models.CharField(max_length=50)
    note_subject = models.CharField(max_length=50)
    note_title = models.CharField(max_length=50)
    note = models.CharField(max_length=800)

    def __str__(self):
        return f"{self.note_subject} ->> {self.note_title}"

