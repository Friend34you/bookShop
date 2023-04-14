from django.urls import path
from .views import OrderView

urlpatterns = [
    path('create/', OrderView.order_create, name='order_create'),
    # path('/<int:id_order>/', OrderView.order_detail, name='order_detail'),
]
