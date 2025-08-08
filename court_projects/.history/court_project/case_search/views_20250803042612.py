from django.shortcuts import render
from .scraper import scrape_case_details
from case_search.utils import save_scraped_data
from django.contrib import messages
a

def search_form(request):
    return render(request, 'case_search/search_form.html')

def search_view(request):
    cnr = request.GET.get("cnr", "").strip().upper()

    if not cnr or len(cnr) != 16:
        messages.error(request, "❌ Invalid CNR format. It must be exactly 16 characters long.")
        return render(request, "case_search/search_result.html")

    try:
        data = scrape_case_details(cnr)
    except Exception as e:
        messages.error(request, f"⚠️ Error occurred while fetching the case: {str(e)}")
        return render(request, "case_search/search_result.html")

    if not data:
        messages.error(request, f"❌ No case found for CNR: {cnr}. Please check the number and try again.")
        return render(request, "case_search/search_result.html")

    case = save_scraped_data(data)
    return render(request, "case_search/search_result.html", {"case": case})
