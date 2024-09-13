from django.shortcuts import render,redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from shopApp.models import user,AddProduct

# Create your views here.
def userRecord(request):
     if request.method=='GET':
        user_objects=user.objects.all()
        return render(request,'userRecord.html',context={'users':user_objects})


def register(request):
    if request.method=='GET':
        return render(request,'register.html')

    if request.method=='POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password!=password2:
            messages.error(request,'passwords do not match')
        else:
            
            user_obj=user.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            password2=password2
            )
        
            user_obj.save()
            messages.success(request,'user created successfully')
            return redirect('login')

def home(request):
    
    if request.method=='GET':
        return render(request,'home.html')


def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj=user.objects.get(username=username,password=password)
        return redirect('dashboard')
    
def dashboard(request):
    if request.method=='GET':
        products=AddProduct.objects.all()
        return render(request,'dashboard.html',context={'products':products})
    
def productRecord(request):
    if request.method == 'GET':
        products = AddProduct.objects.all().order_by('SerialNumber')
        
        for index, product in enumerate(products, start=1):
            product.SerialNumber = index
            product.save()
        
        return render(request, 'ProductRecord.html', context={'products': products})

def addproduct(request):
    if request.method == 'POST':
        ProductName = request.POST.get('Product_Name')
        Description = request.POST.get('description')
        Category = request.POST.get('category')  
        Price = request.POST.get('price')   
        StockQuantity = request.POST.get('stock')  

        AddProduct.objects.create(
            #SerialNumber=next_serial_number,
            ProductName=ProductName,
            Description=Description,
            Category=Category,
            Price=Price,
            StockQuantity=StockQuantity
        )

        messages.success(request, 'Product added successfully')
        return redirect('dashboard')

    return render(request, 'addproduct.html')


def delete(request, id):
   
    product = get_object_or_404(AddProduct, id=id)
    product.delete()

    return render(request,'ProductRecord.html')
   
def logout(requst):
    auth_logout(requst)  
    return render(requst,'home.html')
def edit(request, id):
    product = AddProduct.objects.get(id=id)
    
    if request.method == 'POST':
        product.ProductName = request.POST.get('Product_Name')
        product.Description = request.POST.get('description')
        product.Category = request.POST.get('category')
        product.Price = request.POST.get('price')
        product.StockQuantity = request.POST.get('stock')
        product.save()
        
        messages.success(request, 'Product updated successfully')
        return redirect('dashboard')
    
    return render(request, 'editproduct.html', {'product': product})
