from django.urls import path
from . import views




urlpatterns = [
    path('', views.search_case, name="search_case"),
    path('search_result/<int:pk>', view;)
]
