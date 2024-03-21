from django.urls import path

from users.views.users import RegistrationView, ChangePasswordView, MeView


urlpatterns = [
    path('user/reg/', RegistrationView.as_view(), name='reg'),
    path('user/change-passwd', ChangePasswordView.as_view(),
         name='change_passwd'),
    path('user/profile/', MeView.as_view(), name='profile'),
]
