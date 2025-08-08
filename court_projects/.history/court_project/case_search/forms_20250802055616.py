from django import forms






class CaseSearchForm(forms.Form):
    case_type = forms.CharField(max_length=40, label="Case Type")
    case_number = forms.CharField(max_length=30, label="Case Number")
    year = forms.IntegerField(label='Filing Year')