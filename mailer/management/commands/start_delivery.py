from mailer.models import Distribution, Report
from datetime import datetime
from config.settings import EMAIL_HOST_USER
from django.core.management import BaseCommand
from smtplib import SMTPException
from django.core.mail import EmailMessage


class Command(BaseCommand):

    def handle(self, *args, **options):
        # distibutions = Distribution.objects.filter(is_active=True, timer=datetime.now().strftime('%H:%M:00'))
        distibutions = Distribution.objects.filter(is_active=True)

        for distribution in distibutions:
            print(distribution.messages.title)
            # distribution.status = 'started'
            # distribution.save()

            # email = EmailMessage(
            #     distribution.messages.values_list('title')[0][0],
            #     distribution.messages.values_list('body')[0][0],
            #     EMAIL_HOST_USER,
            #     [x[0] for x in list(distribution.recipients.values_list('address'))],
            # )
            # try:
            #     email.send(fail_silently=False)
            #     distribution.status = 'completed'
            #     distribution.save()
            #
            #     Report.objects.create(status='Successfully', user_id=distribution.user_id)
            #
            # except SMTPException as ex:
            #     Report.objects.create(status='Failed', response=ex, user_id=distribution.user_id)
