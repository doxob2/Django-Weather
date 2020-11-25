from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main),
    path('add/', views.add_city_in_db),
    path('delete/<int:id>', views.delete_city_from_db),
    path('delete-all/', views.delete_all_city_from_db),
]