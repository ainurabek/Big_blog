from blog.models import Companies, Post, Comments
from .serializer import CompaniesSerializer, PostSerializer, CommentsSerializer, CompaniesCreateSerializer, CompaniesEditSerializer, PostCreateSerializer, PostEditSerializer, CommentsCreateSerializer, CommentsEditSerializer, CompaniesDetailSerializer, CompaniesFavoriteSerializer
from rest_framework import  viewsets, generics #APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCompanyOwner, IsPostCompanyOwner, IsCommentsPostCompanyOwner
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class CompaniesFavoriteView(generics.CreateAPIView):
    serializer_class = CompaniesFavoriteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(CompaniesFavoriteView, self).get_serializer_context()
        context.update({
            "user": self.request.user
        })
        return context

class CompaniesListPagination(LimitOffsetPagination):
    default_limit = 2 #po umolchaniyu
    max_page_size = 10000

# ViewSets define the view behavior.
class CompaniesView(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesDetailSerializer
    lookup_field = 'pk'

class CompaniesListView(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    lookup_field='pk'

    pagination_class=CompaniesListPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name', 'address', 'contacts', 'info', 'owner', 'id')
    search_fields = ('name', 'info', 'owner')


class CompaniesDetail(generics.RetrieveAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(CompaniesDetail, self).get_serializer_context()
        context.update({
            "user": self.request.user
        })
        return context

class CompaniesCreateView(generics.CreateAPIView):
    serializer_class=CompaniesCreateSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,) #for ony registered users, they can edit companies

    def get_serializer_context(self):
        context = super(CompaniesCreate, self).get_serializer_context()
        context.update({
            "owner": self.request.user
        })
        return context

class CompaniesEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = Companies.objects.all()
    serializer_class = CompaniesEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsCompanyOwner)


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field='pk'

class PostCreateView(generics.CreateAPIView):
    serializer_class=PostCreateSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated, ) #for ony registered users, they can edit companies

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        company = Companies.objects.get(pk=request.data['company'])
        if company.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'Объявление успешно создано'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'Вы не можете создать объявление от имени компании, которая вам не принадлежит'},
                            status=status.HTTP_400_BAD_REQUEST)




class PostEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = Post.objects.all()
    serializer_class = PostEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsPostCompanyOwner)




class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_field='pk'      

class CommentsCreateView(generics.CreateAPIView):
    serializer_class=CommentsCreateSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated, ) #for ony registered users, they can edit companies

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        company = Companies.objects.get(pk=request.data['company'])
        if company.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'Комментарий успешно создан'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'Вы не можете создать комментарий от имени компании, которая вам не принадлежит'},
                            status=status.HTTP_400_BAD_REQUEST)
class CommentsEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = Comments.objects.all()
    serializer_class = CommentsEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsCommentsPostCompanyOwner)