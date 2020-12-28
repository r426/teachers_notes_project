from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('grade2/', views.view_all_grade2, name='url_all_grade2'),
    path('grade3/', views.view_all_grade3, name='url_all_grade3'),
    path('grade4/', views.view_all_grade4, name='url_all_grade4'),
    path('grade2/<int:post_id>/', views.view_one_grade2, name='url_one_grade2'),
    path('grade3/<int:post_id>/', views.view_one_grade3, name='url_one_grade3'),
    path('grade4/<int:post_id>/', views.view_one_grade4, name='url_one_grade4'),
 ]
