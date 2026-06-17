from django.urls import path
from . import views
from myblog import urls as myblog_urls

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]