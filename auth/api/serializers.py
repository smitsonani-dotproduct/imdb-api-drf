from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    cpassword = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "cpassword"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        username = self.validated_data["username"]
        password = self.validated_data["password"]
        cpassword = self.validated_data["cpassword"]
        email = self.validated_data["email"]

        if password != cpassword:
            raise serializers.ValidationError({"error": "P1 & P2 should be same"})

        user_queryset = User.objects.filter(email=email).exists()
        if user_queryset:
            raise serializers.ValidationError({"error": "Email already exist"})

        account = User(username=username, email=email)
        account.set_password(password)
        account.save()

        return account
