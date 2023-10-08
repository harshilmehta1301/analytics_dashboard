# Create your views here.

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from analytics.models import Log
from dashboard.utils import get_date_range
from dashboard.visualisations.chart import Chart
from dashboard.visualisations.table import Table
from dashboard.visualisations.tile import Tile


class DashboardAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        date_range, period = get_date_range(request_data=request.query_params)
        logs = Log.objects.filter(created__range=date_range)
        tile = Tile(query_set=logs).generate()
        chart = Chart(period=period, filter_range=date_range).generate()
        table = Table(query_set=logs).generate()
        return Response(
            {
                'tile': tile,
                'chart': chart,
                'table': table
            }
        )
