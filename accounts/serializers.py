from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers

from accounts.models import GroupProfile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserDetailsSerializer(serializers.ModelSerializer):
    country_name = serializers.SerializerMethodField(method_name='get_country_name', read_only=True)

    def get_country_name(self, obj):
        return obj.country.name

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'photo', 'dob', 'gender', 'country', 'country_name']
        read_only_fields = ('username', 'email')
        extra_kwargs = {
            'country': {'write_only': True},
        }


class CustomRegisterSerializer(RegisterSerializer):
    def custom_signup(self, request, user):
        role = request.data.get('groups')
        
        user.is_staff = True
        user.save()
        if role:
            user.groups.set(role)
            user.save()

    def save(self,request):
        print("Form save method")
        return self.user


class GroupProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupProfile
        fields = ['role', ]


class GroupSerializers(serializers.ModelSerializer):
    ROLE_CHOICES = (
        1, 'Staff',
        2, 'Seller'
    )
    groupprofile = GroupProfileSerializers()

    class Meta:
        model = Group
        fields = ['id', 'name', 'groupprofile']

    def create(self, validated_data):
        role_data = validated_data.pop('groupprofile')
        group = Group.objects.create(**validated_data)
        GroupProfile.objects.create(group=group, **role_data)
        return group

    # ToDo fix the update of group
    # def update(self, instance, validated_data):
    #     role_data = validated_data.pop('groupprofile')
    #     group = instance.update(**validated_data)
    #     GroupProfile.objects.create(group=group, **role_data)
    #     return group
