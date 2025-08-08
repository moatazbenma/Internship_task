from django.shortcuts import render, redirect, get_object_or_404
from .forms import CaseSearchForm
from .models import QueryLog, CaseData, Order
from django.contrib import messages
from .scraper import scrape_case_details
from .utils import save_scraped_data
# Create your views here.




def search_case(request):
    context = {}
    if request.method == "POST":
        cnr = request.POST.get("cnr")
        try:
            data = scrape_case_details(cnr)
            case = save_scraped_data(data)
            context['case'] = case
        except Exception as e:
            messages.error(request, f"Error: {e}")
    return render(request, "case_search/search_form.html", context)




def search_result(request, query_id):
    query= get_object_or_404(QueryLog, id=query_id)



    try:
        case_data = query.casedata
    except CaseData.DoesNotExist:
        case_data = None

    return render(request, 'case_search/search_result.html',{'queryt':query, 'case_data': case_data} )