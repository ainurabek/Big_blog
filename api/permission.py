from rest_framework.permissions import BasePermission
from blog.models import Companies


class IsCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        company = Companies.objects.get(pk=view.kwargs['pk'])
        if company.owner == request.user:
            return True

