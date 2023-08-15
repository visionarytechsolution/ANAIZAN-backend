from django.db import transaction
from rest_framework import serializers

from category.models import Category, SuggestedCategory,CategoryMedia






class RecursiveField(serializers.Serializer):
        
        
        def to_representation(self, value):
            serializer = self.parent.parent.__class__(value, context=self.context)
            return serializer.data      



class CategorySerializerProduct(serializers.ModelSerializer):
    cat_children = RecursiveField(many=True,required=False)
    class Meta:
        model = Category
        fields = ('name','cat_children',)
