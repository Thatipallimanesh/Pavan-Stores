from django.shortcuts import render, redirect
from django.contrib import messages
from homepage.models import Foodgrain, Flour, Oil, Spice, Dryfruit, Masala, Order, OrderUpdate
import json

# Create your views here.

def index(request):
    foodgrains = Foodgrain.objects.all()
    flours = Flour.objects.all()
    oils = Oil.objects.all()
    spices = Spice.objects.all()
    dryfruits = Dryfruit.objects.all()
    masalas = Masala.objects.all()
    return render(request, "index.html", {'foodgrains':foodgrains, 'flours':flours, 'oils':oils, 'spices':spices, 'dryfruits':dryfruits, 'masalas':masalas})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pincode = request.POST.get('pincode', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, amount=amount, email=email, address=address, city=city, state=state, pin_code=pincode, phone=phone)
        order.save()
        thank = True
        id = order.id
        update = OrderUpdate(order_id=id,update_description="the order has been placed")
        update.save()
        return render(request, "checkout.html", {'thank':thank, 'id':id})
    return render(request, "checkout.html")

def orderTracker(request):
    current_user = request.user.email
    user_orders = Order.objects.filter(email=current_user)
    user_orders = user_orders.order_by('-id')
    all_updates = []
    for i in user_orders:
        id = i.id
        cart = json.loads(i.items_json)
        items_ordered = []
        total_price = 0
        for item in cart:
            items_ordered.append({'qty':cart[item][0], 'name':cart[item][1], 'price':int(cart[item][2])*int(cart[item][0]), 'desc':cart[item][3]})
            total_price = total_price + (int(cart[item][2])*int(cart[item][0]))
        update = OrderUpdate.objects.filter(order_id = id)
        updates = []
        deliveryStatus = False
        for j in update:
            updates.append({'desc':j.update_description, 'time':j.timestamp})
            deliveryStatus = j.delivered
        all_updates.append({'id':id, 'items_ordered':items_ordered, 'total':total_price, 'update':updates, 'deliveryStatus':deliveryStatus})
    return render(request, "orderTracker.html", {'allupdates': all_updates})

def cancel(request):
    if request.method == "POST":
        id = request.POST.get('order_id', '')
        order = Order.objects.filter(id=id)
    return render(request, "orderCancellation.html", {'order':order})

def confirm(request):
    if request.method == "POST":
        id = request.POST.get('order_id', '')
        answer = request.POST.get('answer','')
        if answer == "yes":
            order = Order.objects.filter(id=int(id))
            for i in order:
                # i.cancelled = True
                i.delete()
            messages.info(request, "Your order is cancelled")
            return redirect("orderTracker", )
    return redirect("orderTracker")