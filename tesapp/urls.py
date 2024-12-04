from django.urls import path

from .views import (
    PhotoListView,
    PhotoTagListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
    homeview,
    FileListView,
    subscribe_view,
    team_view,
)
from tesapp import views


app_name = 'photo'

urlpatterns = [
    path('', homeview, name='home'),
    path('events/', PhotoListView.as_view(), name='list'),

    path('events/', PhotoListView.as_view(), name='events'),
    path('articles/', FileListView.as_view(), name='article'),
    path('teams/', team_view, name='teams'),


    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),

    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),

    path('photo/create/', PhotoCreateView.as_view(), name='create'),

    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),

    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
    # path('success/', views.success_view, name='success_page'),
    # path('subscribe/', views.subscribe_view, name='subscribe_view'),

    # path('subscribe_page/', views.subscribe_page , name='subscribe'),
    



    path('contact/', views.contact_view , name='contact'),
    path('subscribe/', views.subscribe_view , name='subscribe'),







]