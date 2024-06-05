from rest_framework import serializers
from collection.models import Item, Collection


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('identifier', 'title', 'description', 'is_published', 'collection')


# class ItemSerializer(serializers.ModelSerializer):
#     identifier = serializers.CharField(max_length=255)
#     title = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     collection_id = serializers.IntegerField()
#
#     def create(self, validated_data: dict):
#         return Item.objects.create(**validated_data)
#
#     def update(self, instance: Item, validated_data: dict):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.collection_id = validated_data.get('collection_id', instance.collection_id)
#         instance.save()
#         return instance
#
#     class Meta:
#         model = Item
#         fields = ('identifier', 'title', 'collection_id', 'description',
#                   'time_create', 'time_update', 'is_published', 'collection_id')


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('title', 'description')