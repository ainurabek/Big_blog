from django.conf.urls import url
from django.urls import path, include
from .views import CompaniesView, CompaniesListView, CompaniesDetail, PostView, CommentsView, CompaniesCreateView, CompaniesEditView, PostCreateView, PostEditView, CommentsCreateView, CommentsEditView, CompaniesFavoriteView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
     path('', include(router.urls)), #main page for api is empty
     path('companies/list/', CompaniesView.as_view({'get':'list'}), name='company_list_api'),
     # path('companies/create/', CompaniesView.as_view({'post': 'create'}), name='company_create_api'),
     path('companies/<int:pk>/', CompaniesView.as_view({'get': 'retrieve','delete':'destroy'}), name='company_api'),

     path('companies/create/', CompaniesCreateView.as_view()),
     path('companies/edit/<int:pk>/', CompaniesEditView.as_view()),


     path('post/list/', PostView.as_view({'get':'list'}),name='post_list_api'),
     # path('post/<int:pk>/', PostView.as_view({'get': 'retrieve','delete':'destroy'}), name='post_api'),
     path('post/create/', PostCreateView.as_view()), 
     path('post/edit/<int:pk>/', PostEditView.as_view()), 
     path('companies/favorite/', CompaniesFavoriteView.as_view()),
     
     


     path('comments/list/', CommentsView.as_view({'get':'list'}), 
        name='comments_list_api'),
     path('comments/create/', CommentsCreateView.as_view()), 
    
     path('comments/edit/<int:pk>/', CommentsEditView.as_view()),
     


 ]

 #int:pk - its primary key for each company it is same id