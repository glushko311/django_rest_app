from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from collection.models import Item, Collection
from collection.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from collection.serializers import ItemSerializer, CollectionSerializer

# # class ItemApiViewSet(viewsets.ModelViewSet):
# class ItemApiViewSet(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.ListModelMixin,
#     viewsets.GenericViewSet
# ):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#     # Расширяй логику получения базовых сущностей здесь
#     def get_queryset(self):
#         pk = self.kwargs.get('pk', None)
#         if pk:
#             return Item.objects.filter(pk=pk)
#
#         return Item.objects.all()
#
#     # path /api/v1/items/collections/
#     @action(methods=['get'], detail=False)
#     def collections(self, request):
#         queryset = Collection.objects.all()
#         return Response({'collection': CollectionSerializer(queryset, many=True).data})
#
#     # path /api/v1/items/7/collection/ - получение коллекции по pk Item
#     @action(methods=['get'], detail=True)
#     def collection(self, request, pk=None):
#         try:
#             item = Item.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Item not found'})
#         return Response({'collection': CollectionSerializer(item.collection, many=False).data})
#
#     def destroy(self, request, *args, **kwargs):
#         print('Delete instance has been started!')
#         res = super().destroy(request, *args, **kwargs)
#         print('Delete instance has been COMPLETED!')
#         return res

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# class ItemApiView(APIView):
#
#     def get(self, request):
#         items_qset = Item.objects.all()
#         return Response({'items': ItemSerializer(items_qset, many=True).data})
#
#     def post(self, request):
#         serializer = ItemSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         # created_item = Item.objects.create(
#         #     identifier=request.data['identifier'],
#         #     title=request.data['title'],
#         #     description=request.data['description'],
#         #     collection_id=request.data['collection_id']
#         #
#         # )
#         return Response({'created_item': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         primary_key = kwargs.get('pk', None)
#         if not primary_key:
#             return Response({'error': "PUT method not allowed"})
#         try:
#             instance = Item.objects.get(pk=primary_key)
#         except:
#             return Response({'error': "Object not exists"})
#
#         serializer = ItemSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'updated_item': serializer.data})

# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

class ItemsListPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 100


class ItemAPIList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    pagination_class = ItemsListPagination
    filter_backends = [SearchFilter,]
    # filterset_fields = ['identifier', 'title', 'is_published', 'time_create', 'time_update']
    search_fields = ['title', 'description']


class ItemAPIView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated,]
    # authentication_classes = [TokenAuthentication, ]


class ItemAPIUpdate(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly,]


class ItemAPIDestroy(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAdminUser]
