from django.urls import path
from artist import views

urlpatterns = [

    path('horror-all-data/', views.HorrorAllData.as_view()),
    path('horror-fav-data/', views.HorrorFavData.as_view()),
    path('search_horror/', views.SearchHorror.as_view()),
    path('viewsethorror/<int:pk>/', views.ViewSetHorror.as_view()),

#------------------------------------------------------------------------

    path('action-all-data/', views.ActionAllData.as_view()),
    path('action-fav-data/', views.ActionFavData.as_view()),
    path('viewsetaction/<int:pk>/', views.ViewSetAction.as_view()),
    path('search_action/', views.SearchAction.as_view()),



]