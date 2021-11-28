
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="shophome"),
    path('about', views.about,name="aboutus"),
    path('contact', views.contact,name="contactus"),
    path('tracker', views.tracker,name="tracking"),
    path('search', views.search,name="searchus"),
    path('productview', views.productview,name="productstat"),
    path('checkout', views.checkout,name="checkoutus"),
]
