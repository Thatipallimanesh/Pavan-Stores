from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from useraccounts.models import User_cart
import http.cookies

# Create your views here.
def signup(request):
    if request.method=="POST":
        first = request.POST['firstname']
        last = request.POST['lastname']
        username = request.POST['username']
        em = request.POST['email']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']
        if p1==p2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=em).exists():
                messages.info(request, 'Email id is already registered')
                return redirect('signup')
            user = User.objects.create_user(first_name=first, last_name=last, username=username, email=em, password=p1)
            user.save()
            email = user.email
            user_cart = User_cart(user_email=email, items_json="{}")
            user_cart.save()
            return redirect('signin')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        return render(request, "signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        p = request.POST['password']
        user = auth.authenticate(username=username, password=p)
        if user is not None:
            auth.login(request, user)
            # user_carts =  User_cart.objects.filter(user_email=user.email)

            # cart = []
            # for i in user_carts:
            #     cart.append({'cart':i.items_json})
            # print(cart)
            # print(user_carts[0].items_json)
            # return HttpResponse(user_carts[0].items_json, content_type="application/json")
            
            # cookie = http.cookies.SimpleCookie()
            # cookie['cart'] = user_carts[0].items_json
            # print("Set-Cookie: " + cookie.output(header="").strip())
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def logout(request):
    # cart = request.COOKIES.get('cart')
    # user_cart = User_cart.objects.filter(user_email=request.user.email)
    # for i in user_cart:
    #     i.items_json = cart
    #     i.save()
    auth.logout(request)
    return redirect('/')
