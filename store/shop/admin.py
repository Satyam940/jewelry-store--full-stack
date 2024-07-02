from django.contrib import admin
from .models import ring,Necklace,Bangles,CartItem,Review_Ring, Review_Necklace
# Register your models here.
admin.site.register(ring)
admin.site.register(Necklace)
admin.site.register(Bangles)
admin.site.register(CartItem)
admin.site.register(Review_Ring)
admin.site.register(Review_Necklace)