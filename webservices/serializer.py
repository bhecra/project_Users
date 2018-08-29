from rest_framework import serializers
from users.models import *

class producto_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'website', 'picture','url')

class user_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id','username','email')

'''class categoria_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'id', 'nombre')'''