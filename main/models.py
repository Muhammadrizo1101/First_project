from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=255)
    status = models.CharField(max_length=25, default="In Progres")


    def __str__(self):
        return self.task 
