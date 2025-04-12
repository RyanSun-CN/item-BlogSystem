from django.urls import path

from album.views import album

urlpatterns = [
    path("<int:uid>", album, name="album")
]