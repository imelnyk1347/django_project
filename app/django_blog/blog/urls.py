from django.urls import path

from .views import posts_list, PostDetail, tags_list, TagDetail, TagCreate, PostCreate


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_detail_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>', TagDetail.as_view(), name='tag_detail_list_url')
]
