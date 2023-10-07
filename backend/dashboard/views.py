# Create your views here.
from datetime import datetime, timedelta

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from analytics.models import Log


class DashboardAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        time_period = request.query_params['time_period']
        if time_period == 'custom':
            date_range = request.query_params['custom_range']
        else:
            filter_data = time_period.split('_')
            value = int(filter_data[0])
            period = filter_data[1]

            end_range = datetime.now()
            start_range = end_range - timedelta(**{period: value})
            date_range = [start_range, end_range]
        logs = Log.objects.filter(created__range=date_range)
        total_calls = logs.count()
        unique_users = logs.values_list('user').distinct().count()
        failed_calls = logs.filter(status='failed').count()
        return Response(
            {
                'unique_users': unique_users,
                'total_calls': total_calls,
                'failed_calls': failed_calls
            }
        )
