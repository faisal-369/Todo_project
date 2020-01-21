from django.db import models


class Todo(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
