from django.db import transaction
from rest_framework import serializers

from category.models import Category, SuggestedCategory


class CategorySerializer(serializers.ModelSerializer):

    """ Category is_active = 1 serializer """
    class Meta:
        model = Category
        fields = ('id', 'code', 'name', 'description', 'slug', 'is_active', 'created_at', 'created_by', 'updated_at', 'updated_by', 'category',)
        read_only_fields = ('id', 'code', 'created_at', 'created_by', 'updated_at', 'updated_by',)


class SuggestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestedCategory
        fields = ('id', 'name', 'description', 'created_at', 'created_by', 'updated_at', 'updated_by', 'category',)
        read_only_fields = ('id', 'code', 'created_at', 'created_by', 'updated_at', 'updated_by',)
