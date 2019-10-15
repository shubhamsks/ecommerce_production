from django import forms
from . import models
class ProductForm(forms.ModelForm):
    # title = forms.CharField(max_length=150)
    # description = forms.CharField(widget = forms.Textarea)
    # price = forms.DecimalField(max_digits=10, decimal_places=2)
    # sale_price = forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = models.Product
        fields = ['title', 'description', 'price', 'sale_price']
class ProductImageForm(forms.ModelForm):
    # image = forms.ImageField()
    # featured = forms.BooleanField()
    # thumbnail = forms.BooleanField(required=False
    class Meta:
        model = models.ProductImage
        fields = ['image', 'featured', 'thumbnail', 'active']
        