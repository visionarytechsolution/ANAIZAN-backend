from django.urls import path
from rest_framework import routers

from shop import views

router = routers.SimpleRouter()
router.register(r'domains', views.DomainViewSet, basename="domain")
router.register(r'stores', views.StoreViewSet, basename="store")
router.register(r'store_managers', views.StoreManagerViewSet, basename="store_manager")
urlpatterns = router.urls
