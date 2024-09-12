from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/test/',TestProductApiView.as_view(), name='test')
    ]
