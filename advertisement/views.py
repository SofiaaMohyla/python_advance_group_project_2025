from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Advertisement
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    context_object_name = 'advertisements'

class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    fields = ['title', 'description']
    template_name = 'advertisement/advertisement_form.html'
    success_url = reverse_lazy('advertisement:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AdvertisementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertisement
    fields = ['title', 'description']
    template_name = 'advertisement/advertisement_form.html'
    success_url = reverse_lazy('advertisement:list')

    def test_func(self):
        return self.get_object().author == self.request.user

class AdvertisementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisement/advertisement_confirm_delete.html'
    success_url = reverse_lazy('advertisement:list')

    def test_func(self):
        return self.get_object().author == self.request.user
