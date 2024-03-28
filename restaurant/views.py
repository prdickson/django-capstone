from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer


def index(request):
    return render(request, "index.html", {})


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
