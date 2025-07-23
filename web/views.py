from rest_framework import viewsets
from .models import Customer, Item, Invoice
from .serializers import CustomerSerializer, ItemSerializer, InvoiceSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def add_customer(request):
    if request.method == 'POST':
        Customer.objects.create(
            name=request.POST['name'],
            mobile=request.POST['mobile'],
            location=request.POST['location']
        )
    return redirect('index')

def add_item(request):
    if request.method == 'POST':
        Item.objects.create(
            name=request.POST['name'],
            price=request.POST['price']
        )
    return redirect('index')
