import datetime
import time
from celery import shared_task
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, Category


#from NewsPortal.NewsPortal import settings

SITE_URL = 'http://127.0.0.1:8000/'
DEFAULT_FROM_EMAIL = 'yas.taras@mail.ru'

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")


@shared_task
def send_notifications(preview, pk, title, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/posts/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email= DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_context, 'text/html')
    msg.send()


@shared_task()
def send_weekly_notifications():
    categories = Category.objects.all()
    for category in categories:
        subscribers = category.subscribers.all()
        posts = Post.objects.filter(category=category, time_date__gte=datetime.datetime.now() - datetime.timedelta(days=7))
        if posts.exists():
            subject = f'Новые статьи в категории {category.get_category_name_display()}'
            html_context = render_to_string(
                'weekly_notifications_email.html',
                {
                    'category': category,
                    'posts': posts,
                    'link': Site.objects.get_current().domain,
                }
            )
            msg = EmailMultiAlternatives(
                subject=subject,
                body='',
                from_email=DEFAULT_FROM_EMAIL,
                to=[s.email for s in subscribers],
            )
            msg.attach_alternative(html_context, 'text/html')
            msg.send()