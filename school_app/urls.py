from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('emp/', views.techer, name='emp'),
    path('s/', views.search, name='search'),
    path('student/<str:pk>/', views.view_std, name='student'),
    path('update_std/<str:pk>/', views.update_std, name='student_update'),
    path('create_std/', views.create_std, name='create_std')
]
