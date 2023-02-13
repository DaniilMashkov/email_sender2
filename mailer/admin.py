from django.contrib import admin
from mailer.models import Distribution, Message, Recipient, Report


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('timer', 'periodicity')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')


@admin.register(Recipient)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('address', )


@admin.register(Report)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('time', 'status', 'response')

