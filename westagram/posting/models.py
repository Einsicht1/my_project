from django.db import models


class Posting(models.Model):
    users = models.ForeignKey('login.Users', on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=100)
    comments = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='comments'

# Create your models here.
