from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name="home"),
      path('api/sending_contact_message/', views.api_test, name="api") #test route
]