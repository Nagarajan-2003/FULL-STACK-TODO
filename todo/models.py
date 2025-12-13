from django.db import models

# Create your models here.
class TodoModel(models.Model):
    title=models.CharField(max_length=10)
    description=models.TextField()
    createdat=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.title