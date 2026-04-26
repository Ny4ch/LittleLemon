from rest_framework import serializers
<<<<<<< HEAD
from .models import Menu, Booking, MenuItem
=======
from .models import Menu, Booking
>>>>>>> 9d926dc5d0c254ce520f18ca7ebd4c90f1e7c0b8

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

<<<<<<< HEAD
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

=======
>>>>>>> 9d926dc5d0c254ce520f18ca7ebd4c90f1e7c0b8
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'