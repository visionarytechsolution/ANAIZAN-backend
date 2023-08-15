from django.db import transaction
from rest_framework import serializers

from category.models import Category, SuggestedCategory,CategoryMedia
from products.models import Product
from products.serializers import ProductSerializer


class CategoryMediaSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('get_type')
    class Meta:
        model = CategoryMedia
        fields = ('id','type','media','catagory')
        read_only_fields = ('id','created_at', 'created_by', 'updated_at', 'updated_by','type')
    def get_type(self,obj):
        try:

            category = Category.objects.get(id=obj.catagory.id)
            obj.typee = category.name
            return obj.typee
        except:
            return None

class RecursiveField(serializers.Serializer):
        
        def to_representation(self, value):
            serializer = self.parent.parent.__class__(value, context=self.context)
            return serializer.data      


class CategorySerializer(serializers.ModelSerializer):
    cat_children = RecursiveField(many=True,required=False)
    """ Category is_active = 1 serializer """
    class Meta:
        model = Category
        fields = ('id', 'code', 'name', 'description', 'slug', 'is_active','cat_children',)
        read_only_fields = ('id', 'code', 'created_at', 'created_by', 'updated_at', 'updated_by',)
        
# Note :  need to change when Big Data Comes 
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        leaf_node = Category.objects.all()
        #print(leaf_node)
        representation['is_leaf'] = instance.is_leaf_node()
        if self.context.get('view') and hasattr(self.context['view'], 'action'):
            if self.context['view'].action == 'retrieve':
                objj = Product.objects.filter(category=instance.id)
                request = self.context.get('request')
                ser = ProductSerializer(objj,many=True,context={'request':request})
                representation['products_from'] = ser.data
                try:
                    catagory_obj = CategoryMedia.objects.get(catagory=instance.id)
                    request = self.context.get('request')
                    catagory_ser = CategoryMediaSerializer(catagory_obj,context = {'request':request})
                    representation['icon'] = catagory_ser.data
                    
                except:
                    representation['icon'] = None
                
            if self.context['view'].action == 'list':

                objj = Product.objects.filter(category=instance.id)[:4]
                request = self.context.get('request')
                ser = ProductSerializer(objj,many=True,context={'request':request})
                representation['products_from'] = ser.data
                try:
                    catagory_obj = CategoryMedia.objects.get(catagory=instance.id)
                    request = self.context.get('request')
                    catagory_ser = CategoryMediaSerializer(catagory_obj,context = {'request':request})
                    representation['icon'] = catagory_ser.data
                except:
                    representation['icon'] = None        
        return representation
    


    
    

class SuggestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestedCategory
        fields = ('id', 'name', 'description', 'created_at', 'created_by', 'updated_at', 'updated_by', 'category',)
        read_only_fields = ('id', 'code', 'created_at', 'created_by', 'updated_at', 'updated_by',)



