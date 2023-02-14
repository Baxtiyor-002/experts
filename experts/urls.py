from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import ExpertListView

urlpatterns = [
    path('', ExpertListView.as_view(), name='article_list')
]