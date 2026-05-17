from django.db import models
from myapp.models import Register


class UserFeedback(models.Model):

    user = models.ForeignKey(Register, on_delete=models.CASCADE)

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject