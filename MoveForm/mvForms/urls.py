
from django.urls import path
from . import views

app_name = 'mvForms'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:moveForm_id>/', views.detail, name = "detail"),
    path('form/', views.form, name = "form"),
]