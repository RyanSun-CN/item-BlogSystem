from django.urls import path

from message.views import message

urlpatterns = [
    path("<int:uid>", message, name="message")
]