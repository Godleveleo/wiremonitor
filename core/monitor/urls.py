from django.urls import path
from monitor import views
from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.conexiones_ssh, name="connect-ssh"),    
    path('añadir-ssh', views.add_ssh, name="add-ssh"),    
    path('estado-connect/<int:id>', views.estado_ssh, name="estado-ssh"),    
    path('monitor-vpn/<int:id>', views.monitor_vpn, name="monitor-vpn"),    
    path('añadir-vpn-server', views.add_vpn_server, name="add-vpnserver"),    
     
    
]
