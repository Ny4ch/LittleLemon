from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
<<<<<<< HEAD
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication # Add this
from rest_framework.permissions import IsAuthenticated

=======
>>>>>>> 9d926dc5d0c254ce520f18ca7ebd4c90f1e7c0b8
from .models import Menu
from .serializers import MenuSerializer

from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})


def index(request):
    return render(request, 'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
<<<<<<< HEAD
    permission_classes = [IsAuthenticated]
=======
>>>>>>> 9d926dc5d0c254ce520f18ca7ebd4c90f1e7c0b8
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    permission_classes = [IsAuthenticated]
=======
>>>>>>> 9d926dc5d0c254ce520f18ca7ebd4c90f1e7c0b8
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer