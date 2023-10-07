from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

# Create your views here.
from users.models import UserToken


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny, ]

    @staticmethod
    def validate(data):
        print('INside')
        email = data.get('email', '').lower()
        password = data.get('password')

        if not email or not password:
            raise ValidationError('Please enter valid credentials.')

        user = User.objects.get(email__iexact=email)
        print('Got user')
        if not user.check_password(raw_password=password):
            raise ValidationError('Please enter valid credentials.')

    def post(self, request):
        try:
            data = request.data
            self.validate(data=data)
            user = User.objects.get(email__iexact=data['email'].lower())
            UserToken.objects.filter(user=user).delete()
            token = UserToken.objects.create(user=user)
            return Response(
                {'token': token.key},
                status=HTTP_200_OK
            )
        except ValidationError as e:
            return Response(str(e), status=HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(APIView):
    def delete(self, request):
        UserToken.objects.filter(user=request.user).delete()
        return Response()
