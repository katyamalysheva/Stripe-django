from rest_framework import serializers
from stripepay.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "description",
            "price",
        )
