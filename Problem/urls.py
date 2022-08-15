from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewset

router=DefaultRouter()
router.register(r'company', CompanyViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]
