from rest_framework import serializers

from analytics.models import Log


class LogSerializer(serializers.ModelSerializer):
    error = serializers.SerializerMethodField()

    class Meta:
        model = Log
        fields = ('id', 'user', 'created', 'status', 'error', 'request', 'response')

    @staticmethod
    def get_error(instance):
        error_message = '-'
        if instance.status == 'failed':
            error_message = instance.response['message']
        return error_message
