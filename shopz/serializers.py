from rest_framework.serializers import ModelSerializer
from .models import Stores


class StoresSerializer(ModelSerializer):

    class Meta:
        model = Stores

        fields = ['phone_number', 'products', 'id', 'manufacturer', 'category', 'email',
                   'quantity', 'price', 'address', 'date', 'name', 'status', 'image', 'owner'
                  ]
