from django import forms






class CaseSearchForm(forms.Form):
    case_type = forms.CharField(max_length=40)