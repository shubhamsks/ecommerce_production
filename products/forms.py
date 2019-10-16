from django import forms
from . import models

# Form for product creation involving only product model
class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['title', 'description', 'price', 'sale_price']

# Form for ProductImage creating involving only ProductImage Model and product is associated in views
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = models.ProductImage
        fields = ['image', 'featured', 'thumbnail', 'active']

# class ProductVariationsForm(forms.ModelForm):
#     class Meta:
#             model = models.Variations
#             fields =['category','title','price'] 
        