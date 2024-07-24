from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import ring,Necklace,CartItem,Review_Ring, Review_Necklace,Order,OrderItem, Bangles, Review_bangle , OTP
from .forms import SignUpForm,Ring_Review,Necklace_Review,OrderForm,Bangle_Review , otpform
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from decimal import Decimal
from django.core.mail import send_mail
from django.utils import timezone
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages





def index(request):
    return render(request , 'index.html')


def ring_list(request):
    rings = ring.objects.all()
    return render(request , 'ring/ring.html',{'rings':rings})
 

@login_required

def ring_review(request, ring_id):
    ring_instance = get_object_or_404(ring, id=ring_id)

    if request.method == 'POST':
        review_form = Ring_Review(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = ring_instance
            review.user = request.user
            review.save()
            return redirect('ring_detail', ring_id=ring_id)
    else:
        review_form = Ring_Review()
    show_form =request.GET.get('show_form', False)

    return render(request, 'ring/item-info.html', {
        'ring': ring_instance,
        'review_form': review_form,
        'show_form':show_form,
    })


def ring_detail(request, ring_id):
    ring_instance = get_object_or_404(ring, id=ring_id)
    reviews = Review_Ring.objects.filter(product=ring_instance).order_by('-create_at')
    review_count = reviews.count()
    

    return render(request, 'ring/item-info.html', {
        'ring': ring_instance,
        'reviews': reviews,
        'review_count':review_count,
    })




@login_required

def ring_like(request, ring_id):
    ring_instance = get_object_or_404(ring, id=ring_id)

    if request.user in ring_instance.liked_by.all():
        ring_instance.liked_by.remove(request.user)
        ring_instance.decrement_likes()
       
        return redirect('ring_detail', ring_id=ring_id)

    ring_instance.increment_likes()
    ring_instance.liked_by.add(request.user)

    return redirect('ring_detail', ring_id=ring_id)



@login_required

def necklace_review(request, necklace_id):
    necklace_obj = get_object_or_404(Necklace, id=necklace_id)

    if request.method == 'POST':
        review_form = Necklace_Review(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = necklace_obj
            review.user = request.user
            review.save()
            return redirect('necklace_details', necklace_id=necklace_id)
    else:
        review_form = Necklace_Review()

    show_form = request.GET.get('show_from' , False)

    return render(request, 'necklace/item-info.html', {
        'necklace': necklace_obj,
        'review_form': review_form,
        'show_form':show_form,
    })



def necklace_list(request):
    necklace = Necklace.objects.all()
    return render(request,'necklace/necklace.html',{'necklace':necklace})


def necklace_details(request , necklace_id):
    necklace = get_object_or_404(Necklace , id=necklace_id)
    reviews = Review_Necklace.objects.filter(product=necklace).order_by('-created_at')
    review_count = reviews.count()
    return render(request,'necklace/item-info.html',{
        'necklace':necklace,
        'reviews':reviews,
        'review_count':review_count,
        
        })

@login_required
def necklace_like(request , necklace_id):
    necklace_instance = get_object_or_404(Necklace , id = necklace_id)
    if request.user in necklace_instance.liked_by.all():
        necklace_instance.liked_by.remove(request.user)
        necklace_instance.decrement_likes()

        return redirect('necklace_details' , necklace_id = necklace_id)

    necklace_instance.increment_likes()
    necklace_instance.liked_by.add(request.user)

    return redirect('necklace_details' , necklace_id = necklace_id)


def bangles_list(request):
    bangles = Bangles.objects.all()
    return render(request , 'bangles/bangles.html',{'bangles': bangles})

@login_required
def bangle_like(request , bangle_id):
    bangle_like = get_object_or_404(Bangles , id=bangle_id)
    if request.user in bangle_like.liked_by.all():
        bangle_like.liked_by.remove(request.user)
        bangle_like.decrement_likes()
        return redirect('bangle_detail', bangle_id=bangle_id)   
    
    bangle_like.increment_likes()
    bangle_like.liked_by.add(request.user)

    return redirect('bangle_detail', bangle_id = bangle_id)



def bangle_detail(request, bangle_id):
    bangle = get_object_or_404(Bangles, id=bangle_id)
   
    reviews = Review_bangle.objects.filter(product=bangle).order_by('-created_at')
    review_count = reviews.count()

    return render(request, 'bangles/item-info.html', {
        'bangle': bangle,
        'reviews': reviews,
        'review_count': review_count
    })



@login_required

def bangle_review(request, bangle_id):
    bangle_obj = get_object_or_404(Bangles, id=bangle_id)

    if request.method == 'POST':
        review_form = Bangle_Review(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = bangle_obj
            review.user = request.user
            review.save()
            return redirect('bangle_detail', bangle_id=bangle_id)
    else:
        review_form = Bangle_Review()

    show_form = request.GET.get('show_from' , False)

    return render(request, 'bangles/item-info.html', {
        'bangle': bangle_obj,
        'review_form': review_form,
        'show_form':show_form,
    })




@login_required

def add_to_cart(request, item_id, model_name):
    content_type = ContentType.objects.get(model=model_name.lower())
    item = get_object_or_404(content_type.model_class(), id=item_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, content_type=content_type, object_id=item_id
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, item_id, model_name):
    content_type = ContentType.objects.get(model=model_name)
    cart_item = get_object_or_404(CartItem, user=request.user, content_type=content_type, object_id=item_id)
    cart_item.delete()
    return redirect('cart_detail')

@login_required

def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.content_object.price * item.quantity for item in cart_items)
    tax_rate = Decimal('5.0') 
    tax_amount = total_amount * (tax_rate / 100)
    tax_amount = '{:.2f}'.format(tax_amount)
    StorePickup = 150
    Discount = 200
    Final_amount = Decimal(tax_amount) + int(total_amount) + StorePickup - Discount
    return render(request, 'cart_detail.html', {
        'cart_items': cart_items,
        'total_amount': total_amount,
        'tax_amount': tax_amount,
        'StorePickup':StorePickup,
        'Discount':Discount,
        'Final_amount': Final_amount
        
        })






def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

           
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.is_active = False
            user.save()

            # Generate and save OTP
            otp = OTP(user=user)
            otp.generate_otp()
            otp.save()

            request.session['user_id'] = user.id
            request.session['user_email'] = user.email

            # Send verification email
            subject = 'Verify Your Account'
            message = render_to_string('registration/otp.html', {
                'user': user,
                'otp_code': otp.otp_code
            })
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]

            email = EmailMessage(subject, message, email_from, recipient_list)
            email.content_subtype = "html"
            email.send()

            return redirect('verify_otp')
        else:
            print(f"Form errors: {form.errors}")  # Debug print
    else:
        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form})

           
def verify_otp(request):
 
    user_id = request.session.get('user_id')

    

    if user_id:
        
        user = get_object_or_404(User, id=user_id)

        user_email = user.email

    if request.method == 'POST':
        form = otpform(request.POST)
        if form.is_valid():
            otp_code = form.cleaned_data['otp_code']

            
            otp = OTP.objects.filter(user=user).first()
            

            if otp and otp_code == otp.otp_code:
                user.is_active = True
                user.save()
                login(request, user)
                return redirect('index')
            else:
                form.add_error('otp_code', 'Invalid OTP')
        else:
            form.add_error(None, 'Form is not valid')
    else:
        form = otpform()
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.get(id=user_id)
            otp = OTP.objects.get(user=user)
            otp_code = otp.otp_code

    return render(request, 'registration/verify_otp.html', {
        'form': form,
        'user_email': user_email,
        'otp_code':otp_code
    })



def resend_otp(request):

    user_id  = request.session.get('user_id')
    if user_id:
        user  = User.objects.get(id = user_id)
        otp = OTP.objects.get(user=user)
        otp.generate_otp()
        request.session ['user_email'] = user.email
        

        Subject = 'Verify your account'
        message = f'Your otp code {otp.otp_code}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(Subject, message, email_from, recipient_list)
    return redirect('verify_otp')


def login_view(request):
    error_message = None

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error_message = "Invalid username or password. Please try again."
        else:
            error_message = "Invalid username or password. Please try again."
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form, 'error_message': error_message})


def logout_view(request):
    if request.method == 'POST':  # For added security, you might still want to use POST
        logout(request)
        return redirect('index')

            
    
@login_required

def create_razorpay_order(request):
    cart_items = CartItem.objects.filter(user=request.user)

    total_amount = sum(item.content_object.price * item.quantity for item in cart_items)
    tax_rate = Decimal('5.0') 
    tax_amount = total_amount * (tax_rate / 100)
    tax_amount = '{:.2f}'.format(tax_amount)
    StorePickup = 150
    Discount = 200
    Final_amount = Decimal(tax_amount) + int(total_amount) + StorePickup - Discount
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user

            total_amount = sum(item.content_object.price * item.quantity for item in cart_items)
            tax_rate = Decimal('5.0')
            order.tax_amount = total_amount * (tax_rate / 100)
            order.store_pickup = Decimal('150')
            order.discount = Decimal('200')
            order.final_amount = total_amount + order.tax_amount + order.store_pickup - order.discount
            order.total_amount = total_amount
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    content_type=item.content_type,
                    object_id=item.object_id,
                    quantity=item.quantity,
                    price=item.content_object.price
                )

            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            razorpay_order = client.order.create({
                'amount': int(order.final_amount * 100),  
                'currency': 'INR',
                'payment_capture': '1'
            })
            order.razorpay_order_id = razorpay_order['id']
            order.save()

            context = {
                'order': order,
                'razorpay_order_id': razorpay_order['id'],
                'razorpay_key': settings.RAZORPAY_KEY_ID,
                'amount': int(order.final_amount * 100),
            }
            return render(request, 'payment/payment_page.html', context)
    else:
        form = OrderForm()

    return render(request, 'payment/create_order.html', {
        
        'form': form,
        'total_amount': total_amount,
        'tax_amount': tax_amount,
        'StorePickup':StorePickup,
        'Discount':Discount,
        'Final_amount': Final_amount
        
        })





@csrf_exempt

def payment_success(request):
    if request.method == 'POST':
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        
        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id', ''),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id', ''),
            'razorpay_signature': request.POST.get('razorpay_signature', '')
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            payment = client.payment.fetch(params_dict['razorpay_payment_id'])
            CartItem.objects.filter(user=request.user).delete()
            order = get_object_or_404(Order , razorpay_order_id=params_dict['razorpay_order_id'])


            Subject = 'Order Confirmation - Your Order has been placed'
            email_from = settings.EMAIL_HOST_USER
            to_email = [request.user.email]
            message = render_to_string('order/email.html', {
                'order':order,
                'payment':payment['amount'] / 100,
                'request':request,
                "delivery_date":"27-07-2024"
            })
            email = EmailMessage(Subject , message , email_from , to_email)
            email.content_subtype = 'html'
            email.send()

        
            


            return render(request, 'payment/payment_success.html', {
                'payment_id': payment['id'],
                'order_id': params_dict['razorpay_order_id'],
                'amount': payment['amount'] / 100,
                'currency': payment['currency'],
                'status': payment['status'],
                'method': payment['method'],
                'email': payment['email'], 
                'contact': payment['contact'],
                'order':order
               
            })
        except razorpay.errors.SignatureVerificationError:
            return render(request, 'payment/payment_failure.html')

    return JsonResponse({'status': 'Invalid request'}, status=400)


@login_required

def order_History(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__content_object')
    return render(request, 'order/order.html', {
        'orders': orders,
    })
    
    
@login_required

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'Cancelled'
    order.save()
    return redirect('order_History')

@login_required

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    # order_count = Order.count()
    
    return render(request, 'order/order_detail.html', {
        'order': order,
        'order_items': order_items,
        # 'order_count':order_count
    })

# import io
# from django.http import HttpResponse
# from django.core import management
# import traceback

# def load_production_data(request):
#     output = io.StringIO()
#     try:
#         management.call_command('load_production_data', stdout=output, stderr=output)
#         return HttpResponse(output.getvalue(), content_type="text/plain")
#     except Exception as e:
#         output.write(f"An error occurred: {str(e)}\n")
#         output.write(traceback.format_exc())
#         return HttpResponse(output.getvalue(), content_type="text/plain", status=500)


