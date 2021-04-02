from django.urls import path
from main_app import views 
 
urlpatterns = [ 
    path('tutorial', views.tutorial_list),
    path('tutorial/<int:pk>/', views.tutorial_detail),
    path('main_app/new/', views.tutorial_list_published)
]