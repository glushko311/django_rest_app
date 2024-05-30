from rest_framework import generics
from collection.models import Item
from collection.serializers import ItemSerializer


class ItemApiView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
