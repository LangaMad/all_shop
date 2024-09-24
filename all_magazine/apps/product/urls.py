from django.urls import path, include
from rest_framework import routers, authentication
from .views import *
router = routers.DefaultRouter()
router.register('products', TestProductViewSet)
# router.register('products', TestProductApiView)
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/cars/retrieve/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view(), name='retrieveupdate'),

    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/products/', TestProductApiView.as_view({'get': 'list'}), name='list'),
    path('api/v1/car/', CarListCreateApiView.as_view(), name='list'),
    # path('api/v1/products/create/', TestProductCreateApiView.as_view(), name='create'),
    # path('api/v1/products/<int:pk>/', TestProductRetrieveApiView.as_view(), name='retrieve'),
    # path('api/v1/products/update/<int:pk>/', TestProductRetrieveUpdateAPIView.as_view(), name='update'),
    # path('api/v1/products/destroy/<int:pk>/', TestProductRetrieveDestroyAPIView.as_view(), name='destroy'),
    # path('api/v1/products/destroy/<int:pk>/', TestProductRetrieveUpdateDestroyAPIView.as_view(), name='updatedestroy')

]