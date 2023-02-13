from django.views.generic import CreateView, TemplateView
from .forms import *
from users.services import send_verify_link, force_str, urlsafe_base64_decode, account_activation_token
from django.shortcuts import redirect
from django.urls import reverse_lazy


class SignedView(TemplateView):
    template_name = 'users/signed.html'


class SignupView(CreateView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    model = CustomUser
    success_url = reverse_lazy('users:signed')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.save()
            send_verify_link(self.object, self.request)
        return super().form_valid(form)


class ActivatedView(TemplateView):
    template_name = 'users/activate.html'


def activate(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = CustomUser.objects.get(pk=uid)

    if account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
    return redirect(reverse_lazy('users:activated'))
