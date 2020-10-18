from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .views import MyItemListView, MyBidListView#, BidCreateView

from welcome.views import ItemUpdateView, ItemDeleteView



app_name="users"
urlpatterns = [
    path("profile/", views.profile, name="profile"),

    path('myitems/', MyItemListView.as_view(), name = 'myitems'),
    path('item/<int:pk>/update', ItemUpdateView.as_view(), name = 'editMyItem'),
    path('mybids/', MyBidListView.as_view(), name = 'mybids'),
    path('item/<int:pk>/delete', ItemDeleteView.as_view(), name = 'deleteMyItem'),

    #path("homepage/", views.homepage, name="homepage"),
    #path('item/new/', ItemCreateView.as_view(), name = 'itemCreate'),
    #path('item/<int:pk>/', ItemDetailView.as_view(), name = 'itemDetail'),
    #path('forgot/', views.forgot, name="Forgot"),
    #path('update/', views.update, name="update"),
    #path('item/<int:pk>/bid', BidCreateView.as_view(), name = 'bidCreate'),
    #path('create/', views.create, name = 'create'),

]
