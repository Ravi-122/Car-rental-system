from django.urls import path
from . import views

urlpatterns=[
    path('',views.Homepage,name='Homepage'),
    path('login/',views.Login,name='Login'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('register/',views.register,name='register'),
    path('logout/',views.Logout,name='Logout'),
    path('feedback/',views.feedback,name='feedback'),
    path('payment/',views.payment,name='payment'),
    
]