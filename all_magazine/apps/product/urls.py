from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/products/',TestProductApiView.as_view(), name='api')
    ]
