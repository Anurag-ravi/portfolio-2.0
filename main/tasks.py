# from celery import shared_task
# from django.core.mail import send_mail
# from portfolio import settings
# from.models import Profile
# import random
# profile = Profile.objects.all().first()

# @shared_task(bind=True)
# def changetheme(self):
#     profile.colortheme = random.randint(0,360)
#     profile.save()
#     return "done"

