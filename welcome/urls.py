from django.urls import path
from . import views

from django.shortcuts import render

#list views
from .views import ItemListView, ItemDetailView, ItemCreateView, ClosedItemListView
from users.views import BidCreateView
app_name="welcome"
urlpatterns = [
    path('', ItemListView.as_view(), name = 'index'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name = 'itemDetail'),
    path('item/<int:pk>/bid', BidCreateView.as_view(), name = 'bidCreate'),
    path('item/new/', ItemCreateView.as_view(), name = 'itemCreate'),
    path('closed/items/', ClosedItemListView.as_view(), name = 'closedItem'),
    path('search/', views.searchItem, name='search'),
]
