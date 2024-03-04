from django.urls import path

import users.views.users

urlpatterns = [
    path('user/reg/', users.views.users.RegistrationView.as_view(), name='reg'),

]
