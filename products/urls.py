from django.urls import path
from rest_framework import routers

from products import views

router = routers.SimpleRouter()
router.register(r'products', views.ProductViewSet, basename="product")
router.register(r'prices', views.ProductPriceViewSet, basename="product price")
router.register(r'medias', views.ProductMediaViewSet, basename="product media")
router.register(r'slider', views.ProductSliderViewSet, basename="product Slider")
urlpatterns = router.urls
