from django.urls import path
from .views import Car_dealersListView, Car_dealersView, TopSellerView

urlpatterns = [
    path('', Car_dealersListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', Car_dealersView.as_view()),
]
