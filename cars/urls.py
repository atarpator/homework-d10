from django.urls import path  
from . import views
  
app_name = "cars"  
urlpatterns = [  
    path("", views.index.as_view(), name="cars_list"),  
    path("<slug:slug>/", views.CarDetail.as_view(), name="car_detail"),  
]