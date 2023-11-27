
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_welcome_email_task(email_address: str, name: str):

    send_mail(
        'HI',
        from_email=None,
        message='''
Hi {name},
Thanks for signing up for our newsletter! You’re joining an amazing community of beauty lovers. From now on you’ll enjoy:
Exciting new product announcementsSpecial offers and exclusive dealsOur unique take on the latest beauty trends
As promised, here is your 10% off your first purchase. Simply use this discount code at the checkout: [CODE]
While you wait for the next issue, check out some of our most popular blog posts:
[LINK 1][LINK 2][LINK 3]
Want more? Follow us on social media and get your daily dose of advice, behind-the-scenes looks and beauty inspiration:
Like us on Facebook / Follow us on Instagram
Best,
[YOUR SIGNATURE]'''.format(name=name),
        recipient_list=[email_address],
        fail_silently=False,
    )
