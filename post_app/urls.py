from django.urls import path
from .views import home, post_detail_view

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail_view, name='post_detail'),
]