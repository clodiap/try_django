from django.urls import path
from products.views import product_detail_view, product_create_view, dynamic_lookup_view, product_delete_view, product_list_view

app_name = 'products'
urlpatterns = [
    # path('product/', product_detail_view, name='product_detail'),
    path('', product_list_view, name='product_list'),
    path('<int:id>/', dynamic_lookup_view, name='product_detail'),
    path('create/', product_create_view, name='product_create'),
    path('<int:id>/delete/', product_delete_view, name='product_delete'),
]
