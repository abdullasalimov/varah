from django.urls import path
from varah.views import index

urlpatterns = [
        path('', index, name='index'),
    ]

