from django.urls import path
from . import views

urlpatterns = [
    path('searcht/',views.searcht,name='searcht'),
]
