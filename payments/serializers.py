
from rest_framework.serializers import ModelSerializer
from .models import Payment


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment

        fields = ['account_balance', 'id', 'account_number', 'registered_date', 
                   'amount', 'updated_date', 'phone_number', 'password', 'name'
                  ]