from datetime import timedelta

from django.db import models
from django.utils import timezone
from rest_framework.authtoken.models import Token

# Create your models here.

USER_TOKEN_EXPIRY_DURATION = 5


class UserToken(Token):
    expires_at = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        app_label = 'users'

    def validate(self):
        """
        This method checks the validity of token with respect to created time
        """
        return self.expires_at is None or self.expires_at > timezone.now()

    def renew(self):
        if USER_TOKEN_EXPIRY_DURATION:
            #  and self.expires_at is not None
            self.expires_at = timezone.now() + timedelta(minutes=USER_TOKEN_EXPIRY_DURATION)
            self.save(update_fields=['expires_at'])

    def delete(self, using=None, keep_parents=False):
        # this will ensure that we are deleting the DRF's token as well
        super().delete()
