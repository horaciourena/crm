from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    """
    This function will display my HomePage
    """
    return render(request, 'accounts/dashboard.html')

def products(request):
    """
    This function will display my ProductsPage
    """
    return render(request, 'accounts/products.html')

def customers(request):
    """
    This function will display my CustomersPage
    """
    return render(request, 'accounts/customers.html')