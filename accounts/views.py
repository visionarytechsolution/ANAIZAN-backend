from allauth.account import app_settings as allauth_settings
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.jwt_auth import set_jwt_cookies
from dj_rest_auth.registration.views import RegisterView, SocialLoginView
from dj_rest_auth.serializers import JWTSerializer, TokenSerializer
from dj_rest_auth.views import LoginView, LogoutView, PasswordChangeView, UserDetailsView
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from .serializers import CustomRegisterSerializer, GroupSerializers, UserDetailsSerializer

User = get_user_model()


class CustomLoginView(LoginView):

    def get_response(self):
        serializer_class = self.get_response_serializer()

        if getattr(settings, 'REST_USE_JWT', False):
            from rest_framework_simplejwt.settings import api_settings as jwt_settings
            access_token_expiration = (timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
            refresh_token_expiration = (timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME)
            return_expiration_times = getattr(settings, 'JWT_AUTH_RETURN_EXPIRATION', False)

            data = {
                'user': self.user,
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
            }

            if return_expiration_times:
                data['access_token_expiration'] = access_token_expiration
                data['refresh_token_expiration'] = refresh_token_expiration

            serializer = serializer_class(
                instance=data,
                context=self.get_serializer_context(),
            )
        elif self.token:
            serializer = serializer_class(
                instance=self.token,
                context=self.get_serializer_context(),
            )
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        user_details = UserDetailsSerializer(instance=self.user, context={'request': self.request})
        response = Response({**serializer.data, **user_details.data}, status=status.HTTP_200_OK)
        if getattr(settings, 'REST_USE_JWT', False):
            set_jwt_cookies(response, self.access_token, self.refresh_token)
        return response


class CustomLogoutView(LogoutView):
    pass


class CustomPasswordChangeView(PasswordChangeView):
    pass


class CustomUserDetailsView(UserDetailsView):
    serializer_class = UserDetailsSerializer


class StaffRegisterView(RegisterView):
    authentication_classes = []
    serializer_class = CustomRegisterSerializer

    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {'detail': _('Verification e-mail sent.')}
        user_details = UserDetailsSerializer(instance=user)
        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
            }
            return JWTSerializer(data, context=self.get_serializer_context()).data
        elif getattr(settings, 'REST_SESSION_LOGIN', False):
            return None
        else:
            serializers = TokenSerializer(user.auth_token, context=self.get_serializer_context())
            return {**serializers.data, **user_details.data}


class CommonUserRegisterView(RegisterView):
    authentication_classes = []

    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {'detail': _('Verification e-mail sent.')}
        user_details = UserDetailsSerializer(instance=user)
        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user_details.data,
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
            }
            return JWTSerializer(data, context=self.get_serializer_context()).data
        elif getattr(settings, 'REST_SESSION_LOGIN', False):
            return None
        else:
            serializers = TokenSerializer(user.auth_token, context=self.get_serializer_context())
            return {**serializers.data, **user_details.data}


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    authentication_classes = (JWTTokenUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Group.objects.filter(groupprofile__role=1)
        else:
            return Group.objects.filter(groupprofile__role=2)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    authentication_classes = (JWTTokenUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class FacebookLogin(SocialLoginView):
    authentication_classes = ()
    permission_classes = ()
    adapter_class = FacebookOAuth2Adapter
    # callback_url = ""


class GoogleLogin(SocialLoginView):
    authentication_classes = ()
    permission_classes = ()
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    # callback_url = ""
