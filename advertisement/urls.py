from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementDetailView,
    AdvertisementCreateView,
    AdvertisementUpdateView,
    AdvertisementDeleteView,
)

urlpatterns = [
    path("", AdvertisementListView.as_view(), name="ad_list"),
    path("<int:pk>/", AdvertisementDetailView.as_view(), name="ad_detail"),
    path("create/", AdvertisementCreateView.as_view(), name="ad_create"),
    path("<int:pk>/update/", AdvertisementUpdateView.as_view(), name="ad_update"),
    path("<int:pk>/delete/", AdvertisementDeleteView.as_view(), name="ad_delete"),
]
