from django.db import models


class Item(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    collection = models.ForeignKey('Collection', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'item'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ("id", )

    def __str__(self):
        return self.title


class Collection(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'collection'
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'
        ordering = ("id", )

    def __str__(self):
        return self.title


