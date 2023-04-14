from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from cart.forms import CartAddProductForm
from shop.models import Customer, Order, Book
from orders.models import Order


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class CustomersListView(ListView):
    template_name = "customer.html"
    model = Customer
    context_object_name = "list_of_all_customers"


class OrdersListView(ListView):
    template_name = "orders.html"
    model = Order
    context_object_name = "list_of_all_orders"


class BooksListView(ListView):
    template_name = "books.html"
    model = Book
    context_object_name = "list_of_all_books"


class BookView(TemplateView):
    template_name = 'book/detail.html'
    model = Book
    context_object_name = "product"

    def book_detail(request, id_book):
        book = get_object_or_404(Book, id_book=id_book)
        cart_product_form = CartAddProductForm()
        return render(request, 'book/detail.html',
                      {'book': book, 'cart_product_form': cart_product_form})


class SearchView(ListView):
    template_name = "search.html"
    model = Order
    context_object_name = "list_of_all_orders"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Order.objects.filter(
            Q(id_customer__first_name__icontains=query) |
            Q(id_customer__last_name__icontains=query)
        ).reverse()


class LkView(ListView):
    template_name = 'lk.html'
    model = Order
    context_object_name = "list_of_all_orders"

    def get_queryset(self):
        query = self.request.user.username
        return Order.objects.filter(
            Q(user__username__icontains=query)).reverse()
