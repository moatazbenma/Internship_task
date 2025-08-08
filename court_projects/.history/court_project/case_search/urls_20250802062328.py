from django.urls import path
from . import views




urlpatterns = [
    path('', views.search_case, name="search_case"),
    path('result/<int:query_id>', views.search_result, name="")
]
