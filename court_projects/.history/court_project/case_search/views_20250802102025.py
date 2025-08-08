from django.shortcuts import render, redirect, get_object_or_404
from .forms import CaseSearchForm
from .models import QueryLog, CaseData, Order
from django.contrib import messages
from .scraper import scrape_case_details
from .utils import save_scraped_data
# Create your views here.




def search_case(request):
    if request.method == 'GET' and 'case_type' in request.GET:
        case_type = request.GET['case_type']
        case_number = request.GET['case_number']
        year = request.GET['year']

        cnr = f"{case_type}{case_number}{year}"
        data = scrape_case_details(cnr)

        if data:
            return render(request, "result.html", {"data": data})
        else:
            return render(request, "result.html", {"error": "No data found."})

    return render(request, "search.html")




def search_result(request, query_id):
    query= get_object_or_404(QueryLog, id=query_id)



    try:
        case_data = query.casedata
    except CaseData.DoesNotExist:
        case_data = None

    return render(request, 'case_search/search_result.html',{'queryt':query, 'case_data': case_data} )