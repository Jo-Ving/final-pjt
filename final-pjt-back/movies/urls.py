from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/picks/', views.picks),
    path('<int:movie_pk>/likes/', views.likes),
    path('<int:review_pk>/review_likes/', views.review_likes),
    path('/recommend1/', views.recommend1),
]