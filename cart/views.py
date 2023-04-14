from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from shop.models import Book
from .models import Cart
from .forms import CartAddProductForm, CartDeleteProductForm


class CartView(TemplateView):
    template_name = 'cart/detail.html'
    model = Cart
    context_object_name = "cart"

    @require_POST
    def cart_add(request, id_book):
        cart = Cart(request)
        book = get_object_or_404(Book, id_book=id_book)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(book=book,
                     quantity=1,
                     update_quantity=cd['update'])
        return redirect('cart_detail')

    @require_POST
    def cart_delete(request, id_book):
        cart = Cart(request)
        book = get_object_or_404(Book, id_book=id_book)
        form = CartDeleteProductForm(request.POST)
        if form.is_valid():
            cart.delete(book=book,
                        quantity=1,
                        )
        return redirect('cart_detail')

    def cart_remove(request, id_book):
        cart = Cart(request)
        book = get_object_or_404(Book, id_book=id_book)
        cart.remove(book)
        return redirect('cart_detail')

    def cart_detail(request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'update_quantity': True})
            item['update_quantity_form'] = CartDeleteProductForm(initial={'update_quantity': True})
        return render(request, 'cart/detail.html', {'cart': cart})
