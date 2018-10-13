from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from carts.models import Cart,CartManager
from myapp.models import Product

# Create your views here.




def cart_home(request):
	#del request.session['cart_id']
	#request.session['cart_id']='12'
	#cart_id = request.session.get('cart_id',None)
	''''if cart_id is None:
		cart_obj = cart_create()
		request.session['cart_id']=cart_obj.id
	else:'''
	#print(request.session)
	#print(dir(request.session))
	#request.session.set_expiry(300) #5 minutes
	#request.session.session_key
	#'session_key', 'set_expiry'
	#key=request.session.session_key
	#print(key)
	#request.session['cart_id']=12 #Set
	#request.session['user']=request.user.username
	cart_obj, new_obj=Cart.objects.new_or_get(request)
	return render(request,'carts/home.html',{'cart': cart_obj})

def cart_update(request):
	product_id = request.POST.get('product_id')
	product_obj = get_object_or_404(Product,id=product_id)
	#print(product_obj)
	cart_obj,new_obj = Cart.objects.new_or_get(request)
	'''if product_obj in cart_obj.products.all():
		cart_obj.products.remove(Product.objects.get(id=product_id))
	else:
		cart_obj.products.add(Product.objects.get(id=product_id))'''
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print('Product is gone')
			return redirect('home')
		cart_obj , new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)
		request.session['cart_items']=cart_obj.products.count()
	return redirect('cart-home')

