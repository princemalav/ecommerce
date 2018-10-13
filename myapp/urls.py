from django.urls import path
from django.conf.urls import include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns=[
   path('home',views.home_page, name='home'),
   path('about',views.about_page,name='about'),
   path('contact',views.contact_page,name='contact'),
   path('login',views.login_page,name='login'),
   path('logout',LogoutView.as_view(),name='logout'),
   path('register',views.register_page,name='register'),
   #path('products',views.Productlistview.as_view()),
   #path('products/<int:pk>/',views.ProductDetailView.as_view()),
   #path('products/<slug>/',views.ProductDetailSlugView.as_view()),
   path('product-fbv',views.product_list_view,name='list view'),
   path('products-fbv/<int:pk>/',views.product_detail_view,name='detail view'),
   #path('featured',views.ProductFeaturedListView.as_view()),
   #path('featured/<int:pk>/',views.ProductFeaturedDetailView.as_view()),
   path('product-featured-list',views.product_featured_list_view,name='featured list'),
   path('product-featured-detail/<int:pk>/',views.product_featured_detail_view,name='featured detail'),
   path('product/<slug>/',views.product_slug_detail,name='slug detail'),
   path('bootstrap',TemplateView.as_view(template_name='bootstrap/example.html')),
   
]