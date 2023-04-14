from django.urls import path
from .views import CartView

urlpatterns = [
    path('', CartView.cart_detail, name='cart_detail'),
    path('cart_add/<int:id_book>/', CartView.cart_add, name='cart_add'),
    path('cart_delete/<int:id_book>/', CartView.cart_delete, name='cart_delete'),
    path('remove/<int:id_book>/', CartView.cart_remove, name='cart_remove'),
]
