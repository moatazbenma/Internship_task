from django.db import models




class QueryLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    c
