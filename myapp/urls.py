from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('verproducto', views.verproducto, name='verproducto'),
    path('login', views.login, name='login'),
    path('login/vender', views.vender, name='vender'),
    path('login/<str:username>', views.logeado, name='logeado'),
    path('productos', views.homeproductos, name='productos'),
    path('productos/<str:nombredeproducto>/', views.verproducto, name='verproducto')

    
    
]