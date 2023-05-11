from django.urls import path
from . import views
urlpatterns = [
    path('',views.books),
    path('<int:id>/',views.book),
]
 # books get,post
 #book get,put,delete