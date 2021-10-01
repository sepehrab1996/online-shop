from rest_framework import serializers
from customers.models import Customer, CustomerImage


class CustomerSerializer(serializers.ModelSerializer):
    images = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='api-customer-image-detail')

    class Meta:
        model = Customer
        exclude = ('last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')


# class CustomerImageSerializer(serializers.ModelSerializer):
#     customer = serializers.ReadOnlyField(source='customer.username')
#
#     class Meta:
#         model = CustomerImage
#         fields = '__all__'


# Register Serializer
class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ('last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = Customer.objects.create_user(validated_data['username'],
                                                validated_data['email'],
                                                validated_data['password'],
                                                validated_data['first_name'],
                                                validated_data['last_name'],
                                                validated_data['identity_code'],
                                                validated_data['age'],
                                                validated_data['gender'],
                                                validated_data['phone_number'],
                                                validated_data['images'],
                                                )

        return customer
