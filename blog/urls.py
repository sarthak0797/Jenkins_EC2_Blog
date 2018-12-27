from django.urls import path
from . import views
from django.conf.urls import include,url


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_list_num, name='post_list_num'),
    url(r'^add_comment/', views.AddComment),
    path('upvote/', views.upvote)
]