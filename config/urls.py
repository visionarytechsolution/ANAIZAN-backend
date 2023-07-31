from django.urls import path

from config import views

urlpatterns = [
    # admin urls
    path('admin/packages/', views.AdminAzPackageListView.as_view()),
    path('admin/packages/add', views.AdminAzPackageCreateView.as_view()),
    path('admin/packages/<int:pk>/', views.AdminAzPackageDetailView.as_view()),

    path('admin/countries/', views.AdminAzCountryListView.as_view()),
    path('admin/countries/add', views.AdminAzCountryCreateView.as_view()),
    path('admin/countries/<int:pk>/', views.AdminAzCountryDetailView.as_view()),

    path('admin/states/', views.AdminAzStateListView.as_view()),
    path('admin/states/add', views.AdminAzStateCreateView.as_view()),
    path('admin/states/<int:pk>/', views.AdminAzStateDetailView.as_view()),

    path('admin/cities/', views.AdminAzCityListView.as_view()),
    path('admin/cities/add', views.AdminAzCityCreateView.as_view()),
    path('admin/cities/<int:pk>/', views.AdminAzCityDetailView.as_view()),

    path('admin/measure_unit/', views.AdminMeasureUnitListView.as_view()),
    path('admin/measure_unit/add', views.AdminMeasureUnitCreateView.as_view()),
    path('admin/measure_unit/<int:pk>/', views.AdminMeasureUnitDetailView.as_view()),

    path('admin/time_unit/', views.AdminTimeUnitListView.as_view()),
    path('admin/time_unit/add', views.AdminTimeUnitCreateView.as_view()),
    path('admin/time_unit/<int:pk>/', views.AdminTimeUnitDetailView.as_view()),

    path('admin/authorization_type/', views.AdminAuthorizationTypeListView.as_view()),
    path('admin/authorization_type/<int:pk>/', views.AdminAuthorizationTypeDetailView.as_view()),

    path('admin/authorization/', views.AdminAuthorizationListView.as_view()),
    path('admin/authorization/add', views.AdminAuthorizationCreateView.as_view()),
    path('admin/authorization/<int:pk>/', views.AdminAuthorizationDetailView.as_view()),

    # simple user or buyer urls
    path('buyer/packages/', views.BuyerAzPackageListView.as_view()),
    path('buyer/packages/<int:pk>/', views.BuyerAzPackageDetailView.as_view()),

    path('buyer/countries/', views.BuyerAzCountryListView.as_view()),
    path('buyer/countries/<int:pk>/', views.BuyerAzCountryDetailView.as_view()),

    path('buyer/states/', views.BuyerAzStateListView.as_view()),
    path('buyer/states/<int:pk>/', views.BuyerAzStateDetailView.as_view()),

    path('buyer/cities/', views.BuyerAzCityListView.as_view()),
    path('buyer/cities/<int:pk>/', views.BuyerAzCityDetailView.as_view()),

    path('buyer/measure_unit/', views.BuyerMeasureUnitListView.as_view()),
    path('buyer/measure_unit/<int:pk>/', views.BuyerMeasureUnitDetailView.as_view()),

    path('buyer/time_unit/', views.BuyerTimeUnitListView.as_view()),
    path('buyer/time_unit/<int:pk>/', views.BuyerTimeUnitDetailView.as_view()),


    # seller or buyer urls
    path('seller/packages/', views.SellerAzPackageListView.as_view()),
    path('seller/packages/<int:pk>/', views.SellerAzPackageDetailView.as_view()),

    path('seller/countries/', views.SellerAzCountryListView.as_view()),
    path('seller/countries/<int:pk>/', views.SellerAzCountryDetailView.as_view()),

    path('seller/states/', views.SellerAzStateListView.as_view()),
    path('seller/states/<int:pk>/', views.SellerAzStateDetailView.as_view()),

    path('seller/cities/', views.SellerAzCityListView.as_view()),
    path('seller/cities/<int:pk>/', views.SellerAzCityDetailView.as_view()),

    path('seller/measure_unit/', views.SellerMeasureUnitListView.as_view()),
    path('seller/measure_unit/<int:pk>/', views.SellerMeasureUnitDetailView.as_view()),

    path('seller/time_unit/', views.SellerTimeUnitListView.as_view()),
    path('seller/time_unit/<int:pk>/', views.SellerTimeUnitDetailView.as_view()),
]
