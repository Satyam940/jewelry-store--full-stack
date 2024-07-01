from django.db import models

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ring(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()
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




    
class Neckless(models.Model):
    name = models.CharField(max_length=10000)
    price = models.DecimalField(max_digits=10000 , decimal_places=2)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    description= models.TextField(max_length=10000)
    stock = models.IntegerField(default=10)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):  
        return self.name
    
    
class Bangles(models.Model):
    name = models.CharField(max_length=10000)
    price = models.DecimalField(max_digits=10000 , decimal_places=2)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    description= models.TextField(max_length=10000)
    stock = models.IntegerField(default=10)
    like_count = models.PositiveIntegerField(default=0)


    
    def __str__(self):
        return self.name
    


class CartItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(default=1)
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.user.username} - {self.content_object.name})"
    


class Review_Ring(models.Model):
    product = models.ForeignKey('ring',on_delete=models.CASCADE , related_name='Ring_reviews')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f' Reviews By {self.user.username}'



