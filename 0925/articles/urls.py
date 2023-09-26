from django.urls import path, include
from . import views

app_name = 'articles'
urlpatterns = [
    path('lunch/<str:menu>/', views.lunch, name='menu'),
    path('p1/<str:hi>/<str:key>', views.p1, name='p1'),
    path('throw/', views.throw, name='throw'), 
    path('catch/', views.catch, name='catch'),
]

