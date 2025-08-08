from django.shortcuts import render
from .forms import CaseSearchForm
from .models import QueryLog
# Create your views here.



def search_case(request):
    if request.method == 'POST':
        form = CaseSearchForm(request.POST)
        if form.is_valid():
            query=QueryLog.objects.create(
                case_type=form.cleaned_data
            )