from rest_framework.serializers import ModelSerializer

from users.models.profile import Profile


class ProfileShortSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'telegram_id',
        )


class ProfileUpdateSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'telegram_id',
        )
