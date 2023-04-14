from django.urls import path
from .views import HomePageView, CustomersListView, OrdersListView, SearchView, BooksListView, BookView, LkView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('customers', CustomersListView.as_view(), name='customers'),
    path('orders', OrdersListView.as_view(), name='orders'),
    path('search', SearchView.as_view(), name='search'),
    path('books', BooksListView.as_view(), name='books'),
    path('book/detail/<int:id_book>/', BookView.book_detail, name='book_detail'),
    path('lk', LkView.as_view(), name='lk'),
    # path('product/detail/<int:id_product>/', GuitarView.product_detail, name='product_detail'),

]