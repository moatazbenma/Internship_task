from django.shortcuts import render
from .scraper import scrape_case_details
from case_search.utils import save_scraped_data

def search_form(request):
    return render(request, 'case_search/search_form.html')

def search_view(request):
    cnr = request.GET.get("cnr")

    if not cnr:
        return render(request, "case_search/search_result.html", {"error": "Please enter a valid CNR."})

    data = scrape_case_details(cnr)
    if not data:
        return render(request, "case_search/search_result.html", {"error": "Case not found or parsing error."})

    case = save_scraped_data(data)
    return render(request, "case_search/search_result.html", {"case": case})
