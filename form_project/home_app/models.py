from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254, null=False)

    def __str__(self):
        return self.name