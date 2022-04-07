from .views import *
from django.urls import path

urlpatterns = [
    path('', home_page_view, name='home'),
]
