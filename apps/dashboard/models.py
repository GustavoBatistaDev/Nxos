from django.db import models
from authentication.models import UserCustom


class Projects(models.Model):
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title