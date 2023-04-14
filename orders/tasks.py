from celery import shared_task
from django.core.mail import send_mail

from bookShop import settings
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ № {order.id}'
    message = f'Уважаемый пользователь {order.first_name},\n\n Вы успешно сделали заказ в нашем магазине. \n\n Номер вашего заказа {order.id}.'
    mail_sent = send_mail(subject, message, settings.EMAIL_HOST_USER, [order.email])
    return mail_sent
