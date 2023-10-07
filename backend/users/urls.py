from django.urls import path

from users.views import UserLoginAPIView, UserLogoutAPIView

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        UserLoginAPIView.as_view(),
        name='login-view'
    ),
    path(
        'logout/',
        UserLogoutAPIView.as_view(),
        name='logout-view'
    ),
]
