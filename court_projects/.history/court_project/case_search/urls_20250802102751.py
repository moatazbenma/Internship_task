from django.urls import path
from . import views




urlpatterns = [
    path('', views.sear, name="search_case"),
    path('search/', views.search_result, name='search_result'),
]
