from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('extracurricular/', views.ExtracurricularView.as_view(), name="extracurricular"),
    path('contact/', views.ContactView.as_view(), name="contact"),
]