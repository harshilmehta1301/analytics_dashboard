from django.urls import path

from dashboard.views import DashboardAPIView

app_name = 'dashboard'

urlpatterns = [
    path(
        '',
        DashboardAPIView.as_view(),
        name='dashboard-view'
    )
]
