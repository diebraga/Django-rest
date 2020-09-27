from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Cars
from .serializers import CarsSerializer, CarsDetailSerializer
from datetime import datetime, timezone, timedelta

class CarsView(ListAPIView):
    queryset = Cars.objects.order_by('-list_date').filter(is_published=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = CarsSerializer
    lookup_field = 'id'

class CarsView(RetrieveAPIView):
    queryset = Cars.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = CarsDetailSerializer
    lookup_field = 'id'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CarsSerializer
    lookup_field = 'id'

    def post(self, request, format=None):
        queryset = Cars.objects.order_by('-list_date').filter(is_published=True)
        data = self.request.data

        sale_type = data['sale_type']
        queryset = queryset.filter(sale_type__iexact=sale_type)

        price = data['price']
        if price == '$0+':
            price = 0
        elif price == '$10,000+':
            price = 10000
        elif price == '$25,000+':
            price = 25000
        elif price == '$50,000+':
            price = 50000
        elif price == '$70,000+':
            price = 70000
        elif price == '$100,000+':
            price = 100000
        elif price == '$250,000+':
            price = 250000
        elif price == '$500,000+':
            price = 500000
        elif price == 'Any':
            price = -1
        
        if price != -1:
            queryset = queryset.filter(price__gte=price)
        
        
        days_passed = data['days_listed']
        if days_passed == '1 or less':
            days_passed = 1
        elif days_passed == '2 or less':
            days_passed = 2
        elif days_passed == '5 or less':
            days_passed = 5
        elif days_passed == '10 or less':
            days_passed = 10
        elif days_passed == '20 or less':
            days_passed = 20
        elif days_passed == 'Any':
            days_passed = 0
        
        for query in queryset:
            num_days = (datetime.now(timezone.utc) - query.list_date).days

            if days_passed != 0:
                if num_days > days_passed:
                    id=query.id
                    queryset = queryset.exclude(id__iexact=id)
        
        has_photos = data['has_photos']
        if has_photos == '1+':
            has_photos = 1
        elif has_photos == '3':
            has_photos = 3
        
        for query in queryset:
            count = 0
            if query.photo_1:
                count += 1
            if query.photo_2:
                count += 1
            if query.photo_3:
                count += 1
            
            if count < has_photos:
                id = query.id
                queryset = queryset.exclude(id__iexact=id)
        
        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)

        serializer = CarsSerializer(queryset, many=True)

        return Response(serializer.data)