from django.shortcuts import render
from .scraper import scrape_case_details
from case_search.utils import save_scraped_data
from django.contrib import messages


def search_form(request):
    return render(request, 'case_search/search_form.html')

def search_view(request):
    cnr = request.GET.get("cnr", "").strip().upper()
    
    if not cnr or len(cnr) != 16:
        return render(request, "case_search/search_result.html", {
            "error": "❌ Invalid CNR format. It must be exactly 16 characters long."
        })

    try:
        data = scrape_case_details(cnr)
    except Exception as e:
        return render(request, "case_search/search_result.html", {
            "error": f"⚠️ Error occurred while fetching the case: {str(e)}"
        })

    if not data:
        return render(request, "case_search/search_result.html", {
            "error": f"❌ No case found for CNR: {cnr}. Please check the number and try again."
        })

    case = save_scraped_data(data)

    return render(request, "case_search/search_result.html", {"case": case})
