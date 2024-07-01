from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),




    path('rings/', views.ring_list, name='ring_list'),
    path('ring/<int:ring_id>/', views.ring_detail, name='ring_detail'),
    path('ring/<int:ring_id>/like/', views.ring_like, name='ring_like'),
    path('ring/<int:ring_id>/review/', views.ring_review, name='ring_review'),
    
    path('neckless/', views.neckless_list, name='neckless_list'),
    path('neckless/<int:neckless_id>/', views.neckless_details, name='neckless_details'),

    path('add_to_cart/<int:item_id>/<str:model_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove_from_cart/<str:model_name>/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),



    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),






]