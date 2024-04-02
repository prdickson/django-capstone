from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"tables", views.BookingViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("api/menu/", views.MenuView.as_view()),
    path("api/menu/<int:pk>/", views.SingleMenuView.as_view()),
    path("api/booking/", include(router.urls)),
]
