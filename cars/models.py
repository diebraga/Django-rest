from django.db import models
from django.utils.timezone import now
from car_dealers.models import Car_dealers

class Cars(models.Model):
    class SaleType(models.TextChoices):
        """
        Creation Car 
        """
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
    

    car_dealer = models.ForeignKey(Car_dealers, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    year = models.IntegerField(max_length=4)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField()
    new = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title
