from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
path('list/<int:x>', views.message_list),
path('single/<int:pk>', views.message_detail),
]
