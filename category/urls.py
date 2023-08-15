from django.urls import path
from rest_framework import routers

from category import views

router = routers.SimpleRouter()
router.register(r'categories', views.CategoryViewSet, basename="category")
router.register(r'suggestions', views.SuggestedCategoryViewSet, basename="suggested_category")
router.register(r'categorymedia', views.CategoryMediaViewSet, basename="suggested_category")
urlpatterns = router.urls