from django.urls import path
from .views import AdvertisementListView, AdvertisementCreateView, AdvertisementUpdateView, AdvertisementDeleteView

app_name = 'advertisement'

urlpatterns = [
    path('', AdvertisementListView.as_view(), name='list'),
    path('create/', AdvertisementCreateView.as_view(), name='create'),
    path('<int:pk>/update/', AdvertisementUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='delete'),
]
