from django.urls import path
from .views import test_views, ProductDetailiew

urlpatterns = [
    path('', test_views, name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailiew.as_view(), name='product_detail')
]