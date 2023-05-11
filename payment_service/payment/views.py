from django.shortcuts import render

from .models import paymentModel

# Create your views here.
def createPayment(request) :
    customerId = request.POST["customerId"]
    sellerId = request.POST["sellerId"]
    payat = request.POST["payat"]
    cartId = request.POST["cartId"]
    numberOfItem = request.POST["numberOfItem"]
    cost = request.POST["cost"]

    pay = paymentModel(customerId,sellerId, payat, cartId, numberOfItem, cost)
    paymentModel.object.create(pay)
    

def deletePayment():
    return