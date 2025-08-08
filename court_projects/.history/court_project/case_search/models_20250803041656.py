from django.db import models

class QueryLog(models.Model):
    cnr_number = models.CharField(max_length=30)  
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cnr_number


class CaseData(models.Model):
    cnr = models.CharField(max_length=30, unique=True)
    case_number = models.CharField(max_length=100)
    petitioner = models.CharField(max_length=255)
    respondent = models.CharField(max_length=255)
    filing_date = models.CharField(max_length=20)
    registration_date = models.CharField(max_length=20)
    hearing_date = models.CharField(max_length=20)
    court_name = models.CharField(max_length=255)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.case_number


class Order(models.Model):
    case = models.ForeignKey(CaseData, on_delete=models.CASCADE, related_name='orders')
    date = models.CharField(max_length=20)
    summary = models.TextField()
    pdf_url = models.URLField()

    def __str__(self):
        return f"Order on {self.date}"
