from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import random

time = timezone.now()

class ring(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_hover = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(max_length=400)
    stock = models.IntegerField(default=10)
    like_count = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_rings')
    
    def __str__(self):
        return self.name
    
    def increment_likes(self):
        self.like_count += 1
        self.save()
    def decrement_likes(self):
        if self.like_count > 0:
            self.like_count -= 1
            self.save()




    
class Necklace(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    image_hover = models.ImageField(upload_to='images/', blank=True, null=True)
    description= models.TextField(max_length=500)
    stock = models.IntegerField(default=10)
    like_count = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_necklace')

    def __str__(self):  
        return self.name
    
    def increment_likes(self):
        self.like_count += 1
        self.save()

    def decrement_likes(self):
        if self.like_count > 0:
            self.like_count -= 1
            self.save()

    
    
    
class Bangles(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    image_hover = models.ImageField(upload_to='images/', blank=True, null=True)
    description= models.TextField(max_length=500)
    stock = models.IntegerField(default=10)
    like_count = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_bangles')

    
    def __str__(self):
        return self.name
    
    def increment_likes(self):
        self.like_count += 1
        self.save()

    def decrement_likes(self):
        if self.like_count > 0:
            self.like_count -= 1
            self.save()
    


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.content_object}"


class Review_Ring(models.Model):
    product = models.ForeignKey('ring',on_delete=models.CASCADE , related_name='Ring_reviews')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f' Reviews By {self.user.username}'



class Review_Necklace(models.Model):
    product = models.ForeignKey('Necklace', on_delete=models.CASCADE, related_name='necklace_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reviews by {self.user.username}'
    

class Review_bangle(models.Model):
    product = models.ForeignKey('Bangles', on_delete=models.CASCADE, related_name='bangle_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reviews by {self.user.username}'


    




class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    store_pickup = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100, default='null')
    state = models.CharField(max_length=100, default='null')
    name = models.CharField(max_length=200)
    status= models.CharField(max_length=100, default='Confirmed')

    def __str__(self):
        return f"Order #{self.id}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.content_object} in Order #{self.order.id}"


class OTP(models.Model):
    user  = models.OneToOneField(User , on_delete=models.CASCADE)
    otp_code = models.IntegerField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.otp_code = random.randint(100000 , 999999)
        self.save()