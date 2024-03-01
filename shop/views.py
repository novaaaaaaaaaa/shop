from django.shortcuts import render, redirect
from.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from .models import Stock, CartItems
# Create your views here.


def home(request):
    return render(request, 'shop/home.html')


def update_profile(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = ProfileForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            messages.success(request, 'saved')
            return redirect('shop:home')
        return render(request, 'shop/update_profile.html', {'form':form})
    
    else:
        messages.success(request, 'log in first')
        return redirect('shop:home')

def add_stock(request):
    if request.method == 'POST':
        form = AddStockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Added')
            return redirect('shop:home')
        return render(request, 'shop/add_stock.html', {'form':form}) 
        
    else:
        form = AddStockForm()
        return render(request, 'shop/add_stock.html', {'form':form})

def display_stock(request):
    stock_items = Stock.objects.all().values()
    context = {
        'items' : stock_items
    }
    return render(request, 'shop/display_stock.html',context)

def add_to_cart(request):
    stock_items = Stock.objects.all()
    if request.method == 'POST':
        form = AddToCart(request.POST)
        if form.is_valid():
            form.save()
            cart_items = CartItems.objects.all()
            latest_record = cart_items[:-1]
            latest_record.custID = request.user.id
           
            latest_record.save()

            return redirect('shop:home')
        return render(request, 'shop/add_to_cart.html', {'form':form, 'stock_items':stock_items})
    else:
        form = AddToCart()
        return render(request, 'shop/add_to_cart.html', {'form':form, 'stock_items':stock_items})

def add_to_shopping_list(request):
    if request.method == 'POST':
        form = AddToShoppingList(request.POST)
        if form.is_valid():
            form.save()
            records = ShoppingListItems.objects.all()
            latest_record = records[len(records)-1]
            print(latest_record)
            current_user = request.user
            latest_record.user = current_user
            latest_record.save()

            return redirect('shop:shopping_list')
        return render(request, 'shop/add_to_shopping_list.html', {'form':form})
    else:
        form = AddToShoppingList()
        return render(request, 'shop/add_to_shopping_list.html', {'form':form})

def shopping_list(request):
    user_list_items = ShoppingListItems.objects.filter(user=request.user).values()

    return render(request, 'shop/shopping_list.html', {'list_items':user_list_items})