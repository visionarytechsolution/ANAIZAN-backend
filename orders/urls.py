from django.urls import path
from rest_framework import routers

from orders import views

router = routers.SimpleRouter()
router.register(r'order_items', views.OrderViewSet, basename="order")
urlpatterns = router.urls
