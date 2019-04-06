from rest_framework.permissions import BasePermission
from blog.models import Companies, Post, Comments


class IsCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        company = Companies.objects.get(pk=view.kwargs['pk'])
        if company.owner == request.user:
            return True


class IsPostCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        post = Post.objects.get(pk=view.kwargs['pk'])
        if post.company.owner == request.user:
            return True

class IsCommentsPostCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        comment = Comments.objects.get(pk=view.kwargs['pk'])
        if comment.company.owner == request.user:
            return True
