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


    path('bangles/', views.bangles_list, name='bangles_list'),
    path('bangle/<int:bangle_id>/', views.bangle_detail, name='bangle_detail'),
    path('bangle/<int:bangle_id>/review/', views.bangle_review, name='bangle_review'),
    path('bangle/<int:bangle_id>/like/', views.bangle_like, name='bangle_like'),




  

    path('add_to_cart/<int:item_id>/<str:model_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove_from_cart/<str:model_name>/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),



    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),



   
    path('create_order/', views.create_razorpay_order, name='create_razorpay_order'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('orders/', views.order_History, name='order_History'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),


]
# import traceback
# from django.http import HttpResponse
# import sys
# from django.core import management
# import io

# def load_production_data(request):
#     output = io.StringIO()
#     try:
#         management.call_command('load_production_data', stdout=output, stderr=output)
#         return HttpResponse(output.getvalue(), content_type="text/plain")
#     except Exception as e:
#         output.write(f"An error occurred: {str(e)}\n")
#         import traceback
#         output.write(traceback.format_exc())
#         return HttpResponse(output.getvalue(), content_type="text/plain", status=500)

    # path('load-production-data/', load_production_data, name='load_production_data'),
    







# def load_data(request):
#     try:
#         management.call_command('load_initial_data')
#         return HttpResponse("Data loaded successfully")
#     except Exception as e:
#         error_info = sys.exc_info()
#         error_tb = traceback.format_exception(*error_info)
#         error_msg = f"Error: {str(e)}\n\nTraceback:\n{''.join(error_tb)}"
#         return HttpResponse(error_msg, content_type="text/plain", status=500)

# def run_migrations(request):
#     management.call_command('migrate_and_create_superuser')
#     return HttpResponse("Migrations applied and superuser created if needed")

# def load_production_data(request):
#     try:
#         output = management.call_command('load_production_data', return_output=True)
#         return HttpResponse(f"Command output: {output}")
#     except Exception as e:
#         error_msg = f"An error occurred: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
#         return HttpResponse(error_msg, content_type="text/plain", status=500)
    
    # path('run-migrations/', run_migrations, name='run_migrations'),
    # path('load-data/', load_data, name='load_data'),