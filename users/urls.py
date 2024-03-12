from django.urls import path

from users.views import users


urlpatterns = [
    path('user/reg/', users.RegistrationView.as_view(), name='reg'),
    path('user/change-passwd', users.ChangePasswordView.as_view(), name='change_passwd'),
    path('user/profile/', users.MeView.as_view(), name='profile'),
]
