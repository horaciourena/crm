from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # For just specific fields use: fields = ['customer', 'product', 'etc', '...']
        fields = '__all__'