from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),




    path('rings/', views.ring_list, name='ring_list'),
    path('ring/<int:ring_id>/', views.ring_detail, name='ring_detail'),  
    path('ring/<int:ring_id>/like/', views.ring_like, name='ring_like'),
    path('ring/<int:ring_id>/review/', views.ring_review, name='ring_review'),

    
    path('necklaces/', views.necklace_list, name='necklace_list'),
    path('necklace/<int:necklace_id>/', views.necklace_details, name='necklace_details'),
    path('necklace/<int:necklace_id>/like/', views.necklace_like, name='necklace_like'),
    path('necklace/<int:necklace_id>/review/', views.necklace_review, name='necklace_review'),


  

    path('add_to_cart/<int:item_id>/<str:model_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove_from_cart/<str:model_name>/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),



    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),



   
    path('create_order/', views.create_razorpay_order, name='create_razorpay_order'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('orders/', views.order_History, name='order_History'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),


    






]