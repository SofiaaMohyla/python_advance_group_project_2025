from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('advertisement.urls')),  # якщо в тебе є додаток advertisement
    path('auth/', include('authentication.urls')),  # підключаємо логін/реєстрацію
]
