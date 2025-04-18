from django.urls import path
from . import views
from .views import PlantCreate, PlantUpdate, PlantDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', PlantDelete.as_view(), name='plants_delete'),
    path('signup/', views.signup, name='signup'),
]