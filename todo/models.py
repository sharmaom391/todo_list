from django.db import models
from django.utils.timezone import now
# Create your models here.
class ToDo(models.Model):
    task=models.CharField(max_length=1000)
    due_date=models.DateField(default=now)
    added_date=models.DateField(default=now)
    choices=(
        ('completed','Completed'),
        ('active','Active'),
        ('overdue','Overdue')
    )
    status=models.CharField(max_length=9,choices=choices,default='active')
    def __str__(self) -> str:
        return self.task