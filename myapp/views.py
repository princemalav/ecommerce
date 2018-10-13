from django.shortcuts import render , redirect , get_object_or_404
from .forms import ContactForm , LoginForm , RegisterForm
from django.contrib.auth import login , authenticate , get_user_model
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from .models import Product
from django.http import Http404
from carts.models import Cart

# Create your views here.
def home_page(request):
	#print(request.session.get('first_name')) #GEt
	content={
	  'title':'Hello World',
	  'context':'Welcome to Home page',
	  'name':'Home page'


	}
	return render(request,'myapp/home_page.html',content)

def about_page(request):
	content={
	  'title':'About Page',
	   'context':'Welcome to About page',
	   'name':'About page'
	}
	return render(request,'myapp/home_page.html',content)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	content={
	  'title':'Contact Page',
	   'context':'Welcome to Contact page',
	   'name':'Contact page',
	   'form': contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	'''if request.method =='POST':
		#print(request.POST)
		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
		print(request.POST.get('content'))'''
	
	return render(request,'contact/contact_view.html',content)

def login_page(request):
	form = LoginForm(request.POST or None)
	context={
		"form":form
	}
	#print("user logged in ")
	#print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)

		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request, user)
			print(request.user.is_authenticated)

			#context['form'] = LoginForm()
			#return redirect(request,'/login')

		else:
			print("Error")

	return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context={
		"form":form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email    = form.cleaned_data.get('email')
		password = form.cleaned_data.get("password")
		
		new_user=User.objects.create_user(username,email,password)
		print(new_user)
    
	return render(request,'auth/register.html',context)




class Productlistview(ListView):
	queryset  = Product.objects.all()
	template_name = 'products/list.html'


class ProductDetailView(DetailView):
	#queryset = Product.objects.all()
	template_name = 'products/detail.html'

	def get_context_data(self , *args,**kwargs):
		context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
		print(context)
		return context

	def get_object(self,*args,**kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instances = Product.objects.get_by_id(pk)
		if instances is None:
			raise Http404('product doesnt exit')
		return instances

def product_list_view(request):
	queryset = Product.objects.all()
	context={
		'object_list' : queryset
	}
	return render(request,'products/list.html',context)


def product_detail_view(request , pk=None, *args, **kwargs):
	instances  = get_object_or_404(Product, pk=pk)

	'''instances = Product.objects.get_by_id(pk)
	if instances is None:
		raise Http404('product doesnt exit')'''
	#qs = Product.objects.filter(id=pk)
	#if qs.exists() and qs.count()==1:
		#instances = qs.first()
	#else:
		#raise Http404("Product Doesnt Exit")
	context={
		'objects' : instances
	}
	return render(request,'products/detail.html',context)


class ProductFeaturedListView(ListView):
	template_name = 'products/list.html'

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Product.objects.featured()

class ProductFeaturedDetailView(ListView):
	#queryset = Product.objects.all()
	template_name = 'products/featured-detail.html'

	def get_queryset(self,*args,**kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		return Product.objects.featured() 

class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = 'products/detail.html'

	def get_object(self,*args,**kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		instances = get_object_or_404(Product, slug=slug)
		if instances is None:
			raise Http404('product doesnt exit')
		return instances

def product_featured_list_view(request):
    instance=Product.objects.filter(featured=True)
    data={
    'objects':instance
    }
    return render(request,'products/featured-list.html',data)
	
def product_featured_detail_view(request,pk=None):
	instance=get_object_or_404(Product,pk=pk,featured=True)
	'''qs=Product.objects.filter(pk=pk,featured=True)
	if qs.exists() and qs.count ==1:
		instance=qs.first()
	else:
		raise Http404('Product not found')'''
	data={
		'objects':instance
	}
	return render(request,'products/featured-detail.html',data)


def product_slug_detail(request,slug=None):
	instance=get_object_or_404(Product,slug=slug)
	cart_obj , new_obj = Cart.objects.new_or_get(request)
	context={'object':instance,'cart':cart_obj}
	return render(request,'products/slugview.html',context)






