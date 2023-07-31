from importlib import import_module

from allauth import app_settings
from allauth.account import views as auth_views
from allauth.socialaccount import providers
from django.urls import include, path, re_path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path("signup/", auth_views.signup, name="account_signup"),
    path("signup/", auth_views.login, name="account_signup"),
    path("login/", auth_views.login, name="account_login"),
    path("logout/", auth_views.logout, name="account_logout"),
    path("password/change/", auth_views.password_change, name="account_change_password"),
    path("password/set/", auth_views.password_set, name="account_set_password"),
    # path("inactive/", auth_views.account_inactive, name="account_inactive"),
    path("email/", auth_views.email, name="account_email"),
    path("confirm-email/", auth_views.email_verification_sent, name="account_email_verification_sent"),
    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", auth_views.confirm_email, name="account_confirm_email"),
    path("password/reset/", auth_views.password_reset, name="account_reset_password"),
    path("password/reset/done/", auth_views.password_reset_done, name="account_reset_password_done"),
    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", auth_views.password_reset_from_key,
            name="account_reset_password_from_key"),
    path("password/reset/key/done/", auth_views.password_reset_from_key_done,
         name="account_reset_password_from_key_done"),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if app_settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [path("social/", include("allauth.socialaccount.urls"))]

provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + ".urls")
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, "urlpatterns", None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns
