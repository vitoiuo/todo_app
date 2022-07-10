from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    status =  (
      ('ongoing', 'Ongoing'),
      ('done', 'Done')
    )

    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    done = models.CharField(max_length=7, choices=status)
    created_on = models.DateTimeField(auto_now_add=True)
    done_on = models.DateTimeField(blank=True, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
      if self.done == 'done':
          self.done_on = timezone.now()
      super(Task, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title