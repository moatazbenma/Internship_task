from django.shortcuts import render
from .scraper import scrape_case_details
from .utils import save_scraped_data

# Fake CNR mapping for demo
def simulate_cnr(case_type, case_number, year):
    # Example: always return a known working CNR
    return "DLSW020991202025"

def search_form(request):
    return render(request, "case_search/search_form.html")

def search_result(request):
    case_type = request.GET.get("case_type")
    case_number = request.GET.get("case_number")
    year = request.GET.get("year")

    cnr = simulate_cnr(case_type, case_number, year)
    data = scrape_case_details(cnr)

    if data:
        case = save_scraped_data(data)
        return render(request, "case_search/search_result.html", {"case": case})
    else:
        return render(request, "case_search/search_result.html", {"error": "Case not found or parsing error."})
