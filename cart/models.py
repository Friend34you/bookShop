from decimal import Decimal
from django.conf import settings
from shop.models import Book


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, book, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        book_id = str(book.id_book)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0,
                                     'price': str(book.current_price)}
        if update_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity
        self.save()

    def delete(self, book, quantity=1):
        """
        Удалить продукт в корзину или обновить его количество.
        """
        book_id = str(book.id_book)
        self.cart[book_id]['quantity'] -= quantity
        self.save()
        if self.cart[book_id]['quantity'] == 0:
            self.remove(book)

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, book):
        """
        Удаление товара из корзины.
        """
        book_id = str(book.id_book)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        book_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        books = Book.objects.filter(id_book__in=book_ids)
        for book in books:
            self.cart[str(book.id_book)]['book'] = book

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
