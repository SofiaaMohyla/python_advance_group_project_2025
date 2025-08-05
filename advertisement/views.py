from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Advertisement
from .forms import AdvertisementForm


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    context_object_name = 'advertisements'
    ordering = ['-created_at']


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisement/advertisement_form.html'
    success_url = reverse_lazy('advertisement:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvertisementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisement/advertisement_form.html'
    success_url = reverse_lazy('advertisement:list')

    def test_func(self):
        advertisement = self.get_object()
        return advertisement.author == self.request.user


class AdvertisementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisement/advertisement_confirm_delete.html'
    success_url = reverse_lazy('advertisement:list')

    def test_func(self):
        advertisement = self.get_object()
        return advertisement.author == self.request.user
