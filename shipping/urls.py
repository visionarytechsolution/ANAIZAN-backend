from django.urls import path
from rest_framework import routers

from shipping import views

router = routers.SimpleRouter()
router.register(r'address', views.AddressViewSet, basename="address")
router.register(r'shippings', views.ShippingViewSet, basename="shipping")
urlpatterns = router.urls
