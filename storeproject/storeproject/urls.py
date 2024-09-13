from django.contrib import admin
from django.urls import path
from shopApp.views import *


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('register/',register,name="register"),
    path('userRecord/',userRecord,name="userRecord"),
    path('home/',home,name="home"),
    path('login/',login,name="login"),
    path('dashboard/',dashboard,name="dashboard"),
    path('addproduct/',addproduct,name="addproduct"),
    path('productRecord/', productRecord, name="productRecord"),
    path('delete/<int:id>/',delete,name="delete"),
    path('logout/', logout, name='logout'),
    path('edit/<int:id>/', edit, name="edit"),

]

