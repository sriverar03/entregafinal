
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   

    path("inicio/", views.inicio_view, name="inicio"),
    
    path("loguear/", views.loguear_view, name="loguear"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
     path("registrar/", views.registro_view, name="registrar"),


]



