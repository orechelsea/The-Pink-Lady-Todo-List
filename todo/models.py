from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
Priority_Choices = [
    ('low', 'low'),
    ('medium', 'medium'),
    ('high', 'high'),
]

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=Priority_Choices, default='low')
    complete = models.BooleanField(default=False)
 

    def __str__(self):
        return self.title

class Meta:
    ordering = ['complete']
