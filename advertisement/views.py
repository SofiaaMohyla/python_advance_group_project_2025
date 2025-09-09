from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Advertisement
from .forms import AdvertisementForm

# 1. Список
class AdvertisementListView(ListView):
    model = Advertisement
    template_name = "advertisement/ad_list.html"
    context_object_name = "ads"
    paginate_by = 5

# 2. Деталі
class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = "advertisement/ad_detail.html"
    context_object_name = "ad"

def _can_manage(user) -> bool:
    # доступ для ролей moderator/admin або суперюзер
    return user.is_authenticated and (user.is_superuser or getattr(user, "role", "") in ("moderator", "admin"))

# 3. Створення
class AdvertisementCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "advertisement/ad_form.html"
    success_url = reverse_lazy("ad_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return _can_manage(self.request.user)

# 4. Редагування
class AdvertisementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "advertisement/ad_form.html"
    success_url = reverse_lazy("ad_list")

    def test_func(self):
        return _can_manage(self.request.user)

# 5. Видалення
class AdvertisementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Advertisement
    template_name = "advertisement/ad_confirm_delete.html"
    success_url = reverse_lazy("ad_list")

    def test_func(self):
        return _can_manage(self.request.user)
