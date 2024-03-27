from django.urls import path, include

from api.spectacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as user_urls
from books.urls import urlpatterns as book_urls
from carts.urls import urlpatterns as cart_urls

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += user_urls
urlpatterns += book_urls
urlpatterns += cart_urls
