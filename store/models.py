from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author=models.CharField(max_length=200)
    language=models.CharField(max_length=50)
    publisher=models.CharField(max_length=200)
    number_of_pages=models.FloatField()
    price=models.FloatField()
    barcode=models.FloatField()
    stock = models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(max_length=10000,blank=True)
    image = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.title


    
