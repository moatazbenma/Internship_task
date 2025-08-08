from django.shortcuts import render, redirect
from .forms import CaseSearchForm
from .models import QueryLog
# Create your views here.



def search_case(request):
    if request.method == 'POST':
        form = CaseSearchForm(request.POST)
        if form.is_valid():
            query=QueryLog.objects.create(
                case_type=form.cleaned_data['case_type'],
                case_number=form.cleaned_data['case_number'],
                year=form.cleaned_data['year'],
                success=False
            )
            return redirect('search_result', query_id=query.id)
        
    else:
        form = CaseSearchForm()
    return render(request, 'case_search/search_form.html', {'form':form})