from django.db import models

SEND_STATUS = [
    ('completed', 'Completed'),
    ('created', 'Created'),
    ('started', 'Started')
]

PERIODS = [
    ('daily', 'Once a day'),
    ('weakly', 'Once a weak'),
    ('monthly', 'Once a month')
]


class Distribution(models.Model):
    timer = models.TimeField(max_length=6, verbose_name='time')
    periodicity = models.CharField(choices=PERIODS, max_length=9)
    status = models.CharField(choices=SEND_STATUS, max_length=12, default='created')
    user = models.ForeignKey('users.CustomUser', verbose_name='User', on_delete=models.CASCADE)
    recipients = models.ManyToManyField('Recipient', verbose_name='recipients')
    messages = models.ManyToManyField('Message', verbose_name='messages')
    is_active = models.BooleanField(default=True)

    class Meta:
        permissions = (('deactivate_user', 'can deactivate user'),
                       ('change_is_active', 'can deactivate distribution'), )


class Message(models.Model):
    title = models.CharField(max_length=80, verbose_name='Title')
    body = models.TextField(max_length=2000, verbose_name='Message body')
    user = models.ForeignKey('users.CustomUser', verbose_name='User', on_delete=models.CASCADE)


class Recipient(models.Model):
    address = models.EmailField(max_length=254, unique=False)
    user = models.ForeignKey('users.CustomUser', verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.address}'


class Report(models.Model):
    time = models.DateTimeField(auto_now=True, verbose_name='time')
    status = models.CharField(max_length=254)
    response = models.CharField(max_length=254, blank=True, null=True)
    user = models.ForeignKey('users.CustomUser', verbose_name='User', on_delete=models.CASCADE)