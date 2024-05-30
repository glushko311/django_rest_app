from rest_framework import serializers
from collection.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('identifier', 'title', 'collection_id')
