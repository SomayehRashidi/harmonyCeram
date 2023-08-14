from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact_us', views.Contactus.as_view(), name='contact_us'),
#     path('contact_us',views.contactus, name='contact_us'),

]


