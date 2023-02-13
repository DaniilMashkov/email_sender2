from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from users.views import CustomUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.conf import settings


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


def send_verify_link(user_object, request):
    current_site = get_current_site(request)
    CustomUser.email_user(
        message=render_to_string('email_template.html', {
            'user': user_object,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user_object.pk)),
            'token': account_activation_token.make_token(user_object),
        }),
        subject='Activate your account',
        from_email=settings.EMAIL_HOST_USER,
        self=user_object
    )


