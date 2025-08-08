from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('case_search.urls', namespace='case_search')),  # 👈 This is crucial
]
