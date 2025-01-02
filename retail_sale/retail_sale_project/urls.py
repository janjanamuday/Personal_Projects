from django.urls import path
from . import views

urlpatterns = [

    path('', views.retail_sale_home, name="retail_sale_home"),
    path('depnd_species/<int:id_dist>/', views.depnd_species, name='depnd_species'),
    path('search_data/', views.search_data, name='search_data'),
]