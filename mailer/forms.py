from .models import *
from django import forms


class DistributionForm(forms.ModelForm):
    timer = forms.TimeField(
        widget=forms.widgets.TimeInput(attrs={'type': 'time'}),
        help_text='when distribution starts')

    messages = forms.ChoiceField()

    recipients = forms.ModelMultipleChoiceField(
        queryset=Recipient.objects.all(),
        help_text='hold "Ctrl" to choose many')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(DistributionForm, self).__init__(*args, **kwargs)

        self.fields['messages'].choices = \
            Message.objects.filter(user_id__exact=self.request.user.id).values_list('id', 'title')

        self.fields['recipients'].queryset = Recipient.objects.filter(user_id__exact=self.request.user.id)

    class Meta:
        model = Distribution
        fields = ['timer', 'periodicity', 'messages', 'recipients']


class MessageForm(forms.ModelForm):
    body = forms.Textarea(attrs={'cols': 80, 'rows': 20})

    class Meta:
        model = Message
        fields = ['title', 'body']
