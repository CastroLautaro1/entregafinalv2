from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from chat.views import chat

urlpatterns = [
    path("chat/", chat, name="chat" ),
]