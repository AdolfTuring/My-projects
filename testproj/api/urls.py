from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MessageList, MessageDetail

urlpatterns = [
path('list/', MessageList.as_view()),
path('single/<int:pk>', MessageDetail.as_view()),
]
