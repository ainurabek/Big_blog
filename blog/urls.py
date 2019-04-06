from django.conf.urls import url
from django.urls import path, include
from . import views


 #company, list youc an import names of defs
# from views import companies_list (name of def)
#  path('', views.companies_list, name='companies_list'),



urlpatterns = [
     path('signup/', views.signup, name='signup'),
     path('', views.companies_list, name='companies_list'),
     path('company/<int:pk>/', views.company_detail, name='company_detail'),
     path('company/new/', views.company_new, name='company_new'),
     path('company/<int:pk>/edit/', views.company_edit, name='company_edit'),
     path('post/list/', views.post_list, name='post_list'),
     path('post/<int:pk>/', views.post_detail, name='post_detail'),
     path('post/new/', views.post_new, name='post_new'),
     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
     path('comments/list/', views.comments_list, name='comments_list'),
     path('comments/<int:pk>/', views.comments_detail, name='comments_detail'),
     path('comments/new/', views.comments_new, name='comments_new'),
     path('comments/<int:pk>/edit/', views.comments_edit, name='comments_edit'),
     
 ]

 