from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView

from cart.models import Cart
from orders.models import Order
from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created


class OrderView(TemplateView):
    template_name = 'order/create.html'
    model = Order
    context_object_name = "order"

    def order_create(request):
        cart = Cart(request)
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                user = request.user
                address = form.cleaned_data['address']
                order = Order.objects.create(user=user,
                                             address=address,
                                             first_name=user.first_name,
                                             last_name=user.last_name,
                                             email=user.email,
                                             )
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             book=item['book'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                # очистка корзины
                cart.clear()
                order_created.delay(order.id)
                return render(request, 'orders/order/created.html',
                              {'order': order})
        else:
            form = OrderCreateForm
        return render(request, 'orders/order/create.html',
                      {'cart': cart, 'form': form})


class OrderItemsListView(ListView):
    template_name = 'order/detail.html'
    model = OrderItem
    context_object_name = "list_of_all_order_items"


