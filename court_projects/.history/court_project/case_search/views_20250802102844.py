from django.shortcuts import render, redirect, get_object_or_404
from .forms import CaseSearchForm
from .models import QueryLog, CaseData, Order
from django.contrib import messages
from .scraper import scrape_case_details
from .utils import save_scraped_data
# Create your views here.




from django.shortcuts import render
from case_search.scraper import scrape_case_details
from case_search.utils import save_scraped_data

def search_form(request):
    return render(request, 'case_search/search_form.html')

def search_result(request):
    if request.method == "GET":
        case_type = request.GET.get("case_type")
        case_number = request.GET.get("case_number")
        year = request.GET.get("year")

        if not (case_type and case_number and year):
            return render(request, "case_search/search_result.html", {"error": "All fields are required."})

        # Construct CNR number
        cnr_number = f"{case_type}{case_number.zfill(6)}{year}"

        data = scrape_case_details(cnr_number)
        if data:
            case = save_scraped_data(data)
            return render(request, "case_search/search_result.html", {"case": case, "orders": case.orders.all()})
        else:
            return render(request, "search_result.html", {"error": "Case not found or parsing error."})


    return render(request, 'case_search/search_result.html',{'queryt':query, 'case_data': case_data} )