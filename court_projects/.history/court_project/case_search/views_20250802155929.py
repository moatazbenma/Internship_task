from django.shortcuts import render
from .scraper import scrape_case_details

def search_form(request):
    return render(request, 'case_search/search_form.html')

def search_view(request):
    case_type = request.GET.get("case_type")
    case_number = request.GET.get("case_number")
    year = request.GET.get("year")

    cnr = f"DLSW02{case_type}{case_number.zfill(4)}{year}"
    data = scrape_case_details(cnr)

    if data:
        latest_order = data["orders"][-1] if data["orders"] else None
        return render(request, 'case_search/search_result.html', {
            "data": data,
            "latest_order": latest_order
        })
    else:
        return render(request, 'case_search/search_result.html', {
            "error": "Case not found or parsing error."
        })
