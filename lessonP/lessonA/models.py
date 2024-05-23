from django.db import models


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tasks'
        verbose_name = 'Task'
        ordering = ['-date']