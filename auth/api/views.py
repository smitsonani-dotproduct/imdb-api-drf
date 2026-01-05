# from django.shortcuts import render
from auth.api.serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

# from auth import models


# Create your views here.
@api_view(["POST"])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data["username"] = account.username
            data["email"] = account.email
            # token = Token.objects.get(user=account).key # if we're using signal from model
            token, created = Token.objects.get_or_create(user=account)
            data["token"] = token.key
            data["response"] = "Registation Successful!"

            ## JWT ##
            # refresh = RefreshToken.for_user(account)
            # data["token"] = {
            #     "refresh": str(refresh),
            #     "access": str(refresh.access_token),
            # }

        else:
            data = serializer.errors

        return Response(data)


@api_view(["POST"])
def logout_view(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(
            data={"response": "Logged out successfully"}, status=status.HTTP_200_OK
        )
