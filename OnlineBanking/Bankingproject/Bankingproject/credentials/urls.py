from . import views
from django.urls import path



urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('new/',views.new,name='new'),
    path('form1/',views.form1,name='form1'),
    path('nn/',views.nn,name='nn'),
    path('logout/',views.logout,name='logout')

]