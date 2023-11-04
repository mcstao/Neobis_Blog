from django.urls import path,include

from users.views import register_view

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', register_view, name='register')
]