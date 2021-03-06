from django.urls import path

from .views import (
    index,
    search,
)

app_name = 'duo'

urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
]
