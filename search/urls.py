from django.urls import path
from . import views

urlpatterns=[
	 #path('product/<slug>/',views.product_slug_detail,name='slug detail'),
	 #path('search/',views.search_product_list_view,name='list'),
	 path('search/',views.SearchProductview.as_view(),name='query'),	
]