from django.db import models

from users.models import User
from goods.models import Products
# Create your models here.


class CartQuerySet(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
           return sum(cart.quantity for cart in self)

        return 0 
        
    

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Created time')

    class Meta:
        db_table = 'Cart'
        verbose_name = 'Cart'
        verbose_name_plural ='Cart'


    objects = CartQuerySet().as_manager()


    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)


    def __str__(self):
        return f'Cart: {self.username} | Product: {self.product.name} | Quantity: {self.quantity}'