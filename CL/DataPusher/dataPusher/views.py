#from urllib import response
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import *
from .models import Account, Destination
from rest_framework.views import APIView
from .serializers import AccountSerializer, DestinationSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class AccountDestinationView(APIView):
    def get(self, request, account_id):
        destinations = Destination.objects.filter(account=account_id)
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
