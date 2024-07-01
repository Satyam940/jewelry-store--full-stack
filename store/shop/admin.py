from django.contrib import admin
from .models import ring,Neckless,Bangles,CartItem,Review_Ring

# Register your models here.
admin.site.register(ring)
admin.site.register(Neckless)
admin.site.register(Bangles)
admin.site.register(CartItem)
admin.site.register(Review_Ring)