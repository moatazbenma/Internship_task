from django.db import models




class QueryLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    case_type = models.CharField(max_length=40)
    case_number = models.CharField(max_length=30)
    year = models.IntegerField()
    success = models.BooleanField(default=False)
    raw_html = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.case_type} {self.case_number}/{self.year}"
    


class CaseData(models.Model):
    query = models.OneToOneField(QueryLog, on_delete=models.CASCADE)
    petitioner = models.CharField(max_length=100)
    