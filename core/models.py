from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField
    done = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now())
    done_on = models.DateTimeField(blank=True, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
      if self.done:
          self.done_on = timezone.now()
      super(Task, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title