from django.db import models

# Create your models here.
class paymentModel(models.Model):
    # id = models.AutoField(primary_key=True)
    customerId = models.IntegerField(default=0)
    sellerId = models.IntegerField(default=0)
    payat = models.CharField(max_length=255)
    cartId = models.IntegerField(default=0)
    numberOfItem = models.IntegerField(default=0)
    cost = models.BigIntegerField(default=0)
    objects = models.Manager()
    def __init__(self, customerId, sellerId, payat, cartId, numberOfItem, cost):
        self.customerId = customerId
        self.sellerId = sellerId
        self.payat = payat
        self.cartId = cartId
        self.numberOfItem = numberOfItem
        self.cost = cost

    class Meta:
        db_table = "payment"
        abstract = True
