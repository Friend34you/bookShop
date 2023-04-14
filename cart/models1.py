from django.conf import settings


class Cart(object):
    def __init__(self, request):
        """
        Инициализация корзины объектом request
        """
        self.session = request.session  # сохраняем текущую сессию
        cart = self.session.get(settings.CART_SESSION_ID)  # пытаемся считать идентификатор корзины изтекущей сессии
        if not cart:  # если в текущей сессии корзины нет
            # создаем новую корзину
            cart = self.session[settings.CART_SESSION_ID] = {}  # новая корзина использует структуру словарь
        self.cart = cart
