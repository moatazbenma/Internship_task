from django.shortcuts import render
from .scraper import scrape_case_details
from .utils import save_scraped_data

def search_form(request):
    return render(request, "case_search/search_form.html")

def search_view(request):
    # You can wire this later. Just make sure it exists for now.
    return render(request, "case_search/search_result.html", {})
