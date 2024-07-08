from django.urls import path
from . import views

urlpatterns = [
    path('transpiler/', views.transpiler),
]

