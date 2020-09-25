from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Car_dealers
from .serializers import Car_dealersSerializer

class Car_dealersListView(ListAPIView):
    """
    Car_dealers list With pagination
    """
    permission_classes = (permissions.AllowAny, )
    queryset = Car_dealers.objects.all()
    serializer_class = Car_dealersSerializer
    pagination_class = None

class Car_dealersView(RetrieveAPIView):
    """
    get Car_dealers by ID
    """
    queryset = Car_dealers.objects.all()
    serializer_class = Car_dealersSerializer

class TopSellerView(ListAPIView):
    """
    List top seller
    """
    permission_classes = (permissions.AllowAny, )
    queryset = Car_dealers.objects.filter(top_seller=True)
    serializer_class = Car_dealersSerializer
    pagination_class = None
