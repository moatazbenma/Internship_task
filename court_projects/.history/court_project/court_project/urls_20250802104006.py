from django.urls import path
from . import views

app_name = 'case_search'

urlpatterns = [
    path('', views.search_form, name='form'),            # For form display
    path('search/', views.search_view, name='search'),   # For search logic/results
]
