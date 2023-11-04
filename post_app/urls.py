from django.urls import path
from .views import home, post_detail_view, add_post, update_post, delete_post

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail_view, name='post_detail'),
    path('post/add/', add_post, name='add'),
    path('post/update/<int:post_id>/', update_post, name='update'),
    path('post/delete/<int:post_id>/', delete_post, name='delete'),
]