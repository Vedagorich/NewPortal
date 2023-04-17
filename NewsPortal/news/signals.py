from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Post_Category
from .tasks import send_notifications


@receiver(m2m_changed, sender=Post_Category)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)


def send_welcome_email(user):
    subject = 'Добро пожаловать на наш сайт!'
    message = render_to_string('accounts/email/welcome_email.html', {'user': user})
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.content_subtype = 'html'
    email.send()


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        send_welcome_email(instance)