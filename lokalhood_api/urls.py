from django.urls import path,include
from lokalhood_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserProfileViewSet)
router.register('shop', views.ShopViewSet)
router.register('request', views.RequestViewSet)

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls))
]
