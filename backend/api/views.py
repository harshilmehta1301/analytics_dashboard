# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils import log_request


class V1APIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response, status = log_request(data=request.data, source='v1')
        return Response(response, status=status)
