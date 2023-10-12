# everycheese/cheeses/urls.py
from django.urls import path
from . import views
from .views import CheeseDeleteView, CheeseListView

app_name = "cheeses"
app_name = 'cheese'
urlpatterns = [
    path(
        route='',
        view=views.CheeseListView.as_view(),
        name='list'
    ),
    path(
    route='add/',
    view=views.CheeseCreateView.as_view(),
    name='add'
    ),
    path(
        route='update/<slug:slug>/',
        view=views.CheeseUpdateView.as_view(),
        name='update'
        ),

    path(
        route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail'),
    path(
        route='<slug:slug>/delete/', 
        view=views.CheeseDeleteView.as_view(),
        name='Delete'),
    
]
    
    

