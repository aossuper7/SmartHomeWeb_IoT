from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=10)

    def __str__(self):
        return self.user_id