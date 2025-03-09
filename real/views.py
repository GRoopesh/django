from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product,Category,Cart
# Create your views here.
def home(request):
    p=Product.objects.all()
    return render(request,'home.html',{'products':p})
def info(request):
    return render(request,'info.html',{})

def search(request):
    pk=request.POST['pin']
    product=Product.objects.filter(pincode=pk)
    return render(request,'home.html',{'products':product})

def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'display.html',{'product':product})
def details(request):
    return render(request,'details.html',{})

def contact(request):
    return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})

def log(request):
    if request.method=='POST':
        username=request.POST['email']
        passw=request.POST['pass']
        if username=='Roopesh' and passw=='123':
            return render(request,'admin.html')
        
        user=authenticate(request,username=username,password=passw)
        if user is not None:
            login(request,user)
            messages.success(request,("you have been logged in succesfully"))
            return redirect('home')
        else:
            messages.success(request,("Bad Credentials"))
            return redirect('home')
    return redirect('home')

def logo(request):
    logout(request)
    messages.success(request,('you have been logged out'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('home')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('home')
        
        # Create the user
        try:
            myuser = User.objects.create_user(username=username, email=email, password=password)
            myuser.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('home')
        except Exception as e:
            messages.error(request, "An error occurred during account creation.")
            return redirect('home')
    
    return render(request, 'home.html')

def category(request):
    pass

def Addcart(request, pk):
    # Get the product instance
    product = get_object_or_404(Product, pk=pk)
    
    # Create a cart entry
    Cart.objects.create(product_id=product)
    messages.success(request,("added to cart  succesfully"))
    return redirect('home')

from django.shortcuts import render
from .models import Cart, Product

def cart(request):
    # Retrieve all product IDs from the cart
    product_ids = Cart.objects.values_list('product_id', flat=True)  # Get a list of product IDs

    # Use the IDs to retrieve the corresponding products
    products = Product.objects.filter(id__in=product_ids)  # Query all products with the matching IDs

    return render(request, 'cart.html', {"products": products})

def addhtml(request):
    return render(request,'addagent.html')

def agents(request):
    return render(request,'agents.html')
