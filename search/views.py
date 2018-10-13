from django.db.models import Q
from django.shortcuts import render
from myapp.models import Product
from django.views.generic.list import ListView

# Create your views here.
'''def search_product_list_view(request):
	query=request.GET.get('q',None)
	print(query)
	if query is not None:
		queryset = Product.objects.filter(title__icontains=query)
	elif query is None:
		queryset = Product.objects.all()

	context={
		'object_list' : queryset
	}
	return render(request,'search/view.html',context)'''

class SearchProductview(ListView):
	template_name='search/view.html'

	def get_context_data(self, **kwargs):
	    context = super(SearchProductview, self).get_context_data(**kwargs)
	    context['query']=self.request.GET.get('q')
	    #searchquery.objects.create(query=query)
	    return context

	def get_queryset(self,*args,**kwargs):
		request = self.request
		print(request.GET)
		query=request.GET.get('q',None)
		print(query)
		if query is not None:
			#lookups=Q(title__icontains=query) | Q(description__icontains=query)
			return Product.objects.search(query)
		return Product.objects.all()
