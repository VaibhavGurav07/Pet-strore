from django.urls import path
from . import views
from petapp.views import MyView

urlpatterns = [
    path("home/",views.home),
    path('about',MyView.as_view())
]