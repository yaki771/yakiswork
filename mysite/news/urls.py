from django.urls import path

from . import views

urlpatterns = [
    
    path('hw/create/', views.homeworkCreate.as_view()),
    path('articles/<int:year>/', views.year_archive),
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]