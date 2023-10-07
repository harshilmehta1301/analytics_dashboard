from django.urls import path

from api.views import V1APIView
from users.views import UserLoginAPIView, UserLogoutAPIView

app_name = 'api'

urlpatterns = [
    path(
        'v1/',
        V1APIView.as_view(),
        name='v1-view'
    )
]
