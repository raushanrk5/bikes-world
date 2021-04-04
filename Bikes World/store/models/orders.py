from django.db import models
from .products import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    completed = models.BooleanField(default=False)


    @staticmethod
    def get_customer_orders(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')