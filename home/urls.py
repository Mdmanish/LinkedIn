from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home', views.home_page, name='home'),
    path('likepost', views.like_post, name='like_post'),
    path('commentpost', views.comment_post, name='comment_post'),
]
