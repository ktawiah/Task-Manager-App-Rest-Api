from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import (
    update_last_login,
)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        data.update(
            {
                "first_name": str(self.user.first_name),
                "last_name": str(self.user.last_name),
                "id": str(self.user.id),
                "email": str(self.user.email),
                "is_active": str(self.user.is_active),
                "inserted_timestamp": str(self.user.inserted_timestamp),
                "updated_timestamp": str(self.user.updated_timestamp),
            }
        )

        return data
