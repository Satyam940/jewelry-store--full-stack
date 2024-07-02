from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import ring,Necklace,CartItem,Review_Ring, Review_Necklace
from .forms import SignUpForm,ReviewForm
from django.contrib.auth.forms import AuthenticationForm


@login_required
def index(request):
    return render(request , 'index.html')


def ring_list(request):
    rings = ring.objects.all()
    return render(request , 'ring/ring.html',{'rings':rings})
 


def ring_detail(request, ring_id):
    Ring =  get_object_or_404(ring, id=ring_id )
     
    return render(request, 'ring/order.html',{'ring':Ring})


@login_required
def ring_review(request, ring_id):
    ring_instance = get_object_or_404(ring, id=ring_id)
  
    reviews = Review_Ring.objects.filter(product=ring_instance).order_by('-id')

    
    if request.method == 'POST':    
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = ring_instance
            review.user = request.user
            review.save()
            return redirect('ring_detail', ring_id=ring_id)
    else:
        review_form = ReviewForm()

    return render(request, 'ring/order.html', {
        'ring': ring_instance,
        'reviews': reviews,
        'review_form': review_form,
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
    reviews = Review_Necklace.objects.filter(product=necklace_obj).order_by('-id')

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = necklace_obj
            review.user = request.user
            review.save()
            return redirect('necklace_details', necklace_id=necklace_id)
    else:
        review_form = ReviewForm()

    return render(request, 'necklace/order.html', {
        'necklace': necklace_obj,
        'reviews': reviews,
        'review_form': review_form
    })



def necklace_list(request):
    necklace = Necklace.objects.all()
    return render(request,'necklace/necklace.html',{'necklace':necklace})


def necklace_details(request , necklace_id):
    necklace=get_object_or_404(Necklace , id=necklace_id)
    stock = range(1,necklace.stock+1)
    return render(request,'necklace/order.html',{'necklace':necklace , 'stock':stock})

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





@login_required
def add_to_cart(request, item_id, model_name):
    content_type = ContentType.objects.get(model=model_name)
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
    return render(request, 'cart_detail.html', {'cart_items': cart_items})






def signup(request):
    if request.method=='POST':
        form= SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            form.save()
            login(request , user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render( request , 'registration/register.html', {'form':form})



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




            
    






