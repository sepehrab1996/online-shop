from django.http import Http404
from knox.models import AuthToken
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from customers.models import CustomerImage, Customer
from customers.api.serializers import CustomerSerializer, CustomerRegisterSerializer


# class CustomerImageDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return CustomerImage.objects.get(pk=pk)
#         except CustomerImage.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         customer_image = self.get_object(pk)
#         res = dict()
#         res['customer_image'] = CustomerImageSerializer(customer_image, many=False).data
#         return Response(res)
#
#
# class CustomerList(APIView):
#     def get(self, request, format=None):
#         response = dict()
#         response['customers'] = CustomerSerializer(Customer.objects.all(), context={'request': request},
#                                                    many=True).data
#         return Response(response)


class CustomerRegister(generics.GenericAPIView):
    serializer_class = CustomerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.save()
        return Response({
            "customer": CustomerSerializer(customer, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(customer)[1]
        })
