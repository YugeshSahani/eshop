from django.db import models

from decimal import Decimal, ROUND_DOWN


# Create your models here.



class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # no table for this model



class Contact(TimeStampModel):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Newsletter(TimeStampModel):
    email = models.EmailField()


    def __str__(self):
        return f"{self.email}"
    

class Customer(TimeStampModel):
    fname = models.CharField(max_length=25)
    mname = models.CharField(max_length=25, blank=True)
    lname = models.CharField(max_length=25)
    contact = models.BigIntegerField(blank=True, null=True)
    location = models.CharField(max_length=25)


class Category(TimeStampModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TrendingItemCategory(TimeStampModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class TargetCustomer(TimeStampModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(TimeStampModel):
    name = models.CharField(max_length=50)

    def __str__(self):
            return self.name

class Item(TimeStampModel):
    STATUS_CHOICES = [
        ("in stock", "In Stock"),
        ("out of stock", "Out of Stock"),
    ]
    name = models.CharField(max_length=200)
    detail = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discont_percent = models.DecimalField(max_digits=4, decimal_places=2)
        
    def discounted_price(self):
        discount = self.price * (self.discont_percent / 100)
        discounted_price = self.price - discount
        return discounted_price.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

    featured_image = models.ImageField(upload_to="item_images/%Y/%m/%d", blank=False)
    other_image = models.ImageField(upload_to="item_images/%Y/%m/%d", blank=False)
    target_customer = models.ManyToManyField(TargetCustomer)
    seller = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    listed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="in stock")
    views_count = models.PositiveBigIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    trending_items_category = models.ForeignKey(TrendingItemCategory, default=1 ,on_delete=models.CASCADE)
   

    def __str__(self):
        return self.name
    

class Comment(TimeStampModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} | {self.comment[:70]}"





