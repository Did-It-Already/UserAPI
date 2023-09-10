from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ["user_id", "name", "last_name", "email", "profile_picture", "image_url", "theme"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("profile_picture")
        return representation