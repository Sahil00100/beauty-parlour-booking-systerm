from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from.forms import UserForm,BookingForm
from django import forms
# Create your views here.
import datetime
from.models import *
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import EmailMessage,send_mail,BadHeaderError
from django.contrib import messages
#index page views
def index_view(request):
   
    return render(request, 'index.html',{})

def booking_view(request,id):
    form=BookingForm()
    if request.method=='POST':
        date=request.POST['date']
        #mobile=request.POST['mobile']
        time=request.POST['time']
              
        print(date)
        

        order=Order.objects.get_or_create(
            user=User.objects.get(username=request.user),
            product=Product.objects.get(id=id),
            date=date,
            time=time,
            mobile_no='1234567899',
            )
        
      
    else:    
        form=BookingForm
    return render(request,'book.html',{'form':form})
#registration

def register_view(request):
    print(1)
    if request.method=='POST':
        print(2)
        form=UserForm(request.POST)
        if form.is_valid():
            print(3)
            user=form.create_user()
            user.save()
            return redirect('login')
        else:
            print('failed')
    else:
        form=UserForm()
    return render(request, 'signup.html',{'form':form})

#login

def login_view(request):
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            print('invalid username or password') 
            messages.add_message(request, messages.INFO, 'invalid username or password')   
    return render(request,'login.html',{})

#log out
def logout_view(request):
    logout(request)
    print('logout success!')
    return redirect('login')







def orders_view(request):
    orders=Order.objects.all()
    return render(request,'appoiments.html',{'orders':orders,'media_url':settings.MEDIA_URL})



def searvice_view(request):
    product_male=Product.objects.filter(gender='male')
    product_female=Product.objects.filter(gender='female')
    return render(request,'service.html',{'f':product_female,'m':product_male})
   



def checkout_view(request,id):
    product=Mobile.objects.get(id=id)
    total=product.price


    if request.method=="POST":
        print('yes')
        user=User.objects.get(username=request.user)
        cart=Cart.objects.filter(user=request.user)
        
                    
        name=request.POST['name']
        #price=request.POST['price']
        mobile_no=request.POST['mobile']
        pincode=request.POST['pincode']
        house=request.POST['house']
        street=request.POST['street']
        landmark=request.POST['landmark']
        town=request.POST['town']
        state=request.POST['state']
        date=datetime.datetime.today()

        
        Order.objects.get_or_create(
                user=user,
                product=product,
                name=name,
                price=total,
                mobile_no=mobile_no,
                pincode=pincode,
                house=house,
                street=street,
                landmark=landmark,
                town=town,
                state=state,
                date=date,
            )
           
        return redirect('orders')
    else:
        print('nothing')


    return render(request,'checkout.html',{'total':total})

def gallery_view(request):
    g=Gallery.objects.all()
    return render(request,'gallery.html',{'g':g,'media_url':settings.MEDIA_URL})