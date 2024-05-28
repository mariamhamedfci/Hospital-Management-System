
from django.urls import path # type: ignore
from .views import About ,Home,contact,Login,Logout_admin

urlpatterns = [
   path('about/',About , name = 'About'),
   path('',Home, name = 'Home'),
   path('contact/',contact, name = 'contact'),
    path('Admin_login/',Login, name = 'login'),
    path('Logout/',Logout_admin, name = 'Logout'),

]
