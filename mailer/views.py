from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from users.models import CustomUser
from blog.models import Blog


class HomeListView(ListView):
    template_name = 'home.html'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['users'] = CustomUser.objects.all().exclude(is_superuser=True)
        context['distributions'] = Distribution.objects.all()
        context['active_distributions'] = Distribution.objects.filter(status='started')
        context['articles'] = Blog.objects.order_by('?')[:3]
        return context


class ReportListView(LoginRequiredMixin, ListView):
    template_name = 'mailer/report_list.html'
    model = Report

    def get_queryset(self):
        return Report.objects.filter(user_id=self.request.user.id)


class DistributionListView(LoginRequiredMixin, ListView):
    template_name = 'mailer/distribution_list.html'
    model = Distribution

    def get_queryset(self):
        return Distribution.objects.filter(user_id=self.request.user.id)


class DistributionManagerListView(PermissionRequiredMixin, ListView):
    template_name = 'mailer/distribution_list.html'
    model = Distribution
    permission_required = ('mailer.deactivate_user', 'mailer.change_is_active')

    def get_context_data(self, **kwargs):
        context = super(DistributionManagerListView, self).get_context_data(**kwargs)
        context['manage_users'] = CustomUser.objects.all()\
            .exclude(is_superuser=True).exclude(pk=self.request.user.id)
        return context


def switch_distribution_status(request, pk):
    obj = get_object_or_404(Distribution, pk=pk)

    if obj.is_active:
        obj.is_active = False
    else:
        obj.is_active = True

    obj.save()
    return redirect(request.META.get('HTTP_REFERER'))


def switch_user_status(request, pk):
    obj = get_object_or_404(CustomUser, pk=pk)

    if obj.is_active:
        obj.is_active = False
    else:
        obj.is_active = True

    obj.save()
    return redirect(request.META.get('HTTP_REFERER'))


class DistributionCreateView(LoginRequiredMixin, CreateView):
    form_class = DistributionForm
    template_name = 'mailer/distribution_form.html'
    success_url = reverse_lazy('mailer:distributions')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(DistributionCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class DistributionUpdateView(LoginRequiredMixin, UpdateView):
    form_class = DistributionForm
    model = Distribution
    success_url = reverse_lazy('mailer:distributions')
    Distribution.status = 'created'

    def get_form_kwargs(self):
        kwargs = super(DistributionUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class DistributionDeleteView(LoginRequiredMixin, DeleteView):
    model = Distribution
    success_url = reverse_lazy('mailer:distributions')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        return Message.objects.filter(user_id=self.request.user.id)


class MessageCreateView(LoginRequiredMixin, CreateView):
    form_class = MessageForm
    template_name = 'mailer/message_form.html'
    success_url = reverse_lazy('mailer:messages')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    form_class = MessageForm
    model = Message
    success_url = reverse_lazy('mailer:messages')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailer:messages')


class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient

    def get_queryset(self):
        return Recipient.objects.filter(user_id=self.request.user.id)


class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    fields = ('address',)
    success_url = reverse_lazy('mailer:recipients')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    fields = ('address',)
    model = Recipient
    success_url = reverse_lazy('mailer:recipients')


class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    success_url = reverse_lazy('mailer:recipients')
