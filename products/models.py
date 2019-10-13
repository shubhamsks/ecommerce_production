from django.db import models
from django.urls import reverse

# Product model to store the products 
class Product(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=6,null = True, blank = True)
    slug = models.SlugField(unique = True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    class Meta:
        unique_together = ('title', 'slug')
    
    def get_absolute_url(self):
        return reverse('single-product',kwargs={'slug':self.slug})

# This model stores the images related to single product
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='products/images', default = 'default.jpg')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) 
class VariationsManager(models.Manager):
    def all(self):
        return super(VariationsManager, self).filter(active = True)
    def sizes(self):
        return self.all().filter(category='size')
    def colors(self):   
        return self.all().filter(category = 'color')

VAR_CATEGORIES = (
    ('size', 'size'),
    ('color', 'color'),
    ('package','package'),
)
# This model stores the Variations in the product like if its a tshirt then size and color are variations .
class Variations(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length = 120, choices = VAR_CATEGORIES, default = 'size')
    title = models.CharField(max_length=120)
    image = models.ForeignKey(ProductImage, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    object = VariationsManager()
    objects = models.Manager()
    def __str__(self):
        return self.title   
    
    