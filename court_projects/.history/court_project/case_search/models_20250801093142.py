from django.db import models




class QueryLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    case_type = models.CharField(max_length=40)
    case_number = models.CharField(max_length=30)
    year = models.IntegerField
