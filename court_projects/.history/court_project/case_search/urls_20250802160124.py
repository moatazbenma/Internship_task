from django.urls import path
from . import views

app_name = 'case_search'  # Important for namespacing in templates

urlpatterns = [
    path('', views.search_form, name='search_form'),      # form at /
    path('results/', views.search, name='search'),         # handles GET & shows results
]