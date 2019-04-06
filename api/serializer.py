#analog forms.py

from blog.models import Companies, CompaniesFavorite, Post, Comments
from rest_framework import routers, serializers


# Serializers define the API representation.
class CompaniesFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaniesFavorite
        fields = ('company',)

    def create(self, validated_data):
        user = self.context.get('user')
        company = validated_data['company']
        favorite = CompaniesFavorite.objects.filter(user=user, company=company)
        if favorite:
            favorite.delete()

        else:
            fav_company = CompaniesFavorite.objects.create(user=user, **validated_data)
            fav_company.save()
            return fav_company
        

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta: #copy from forms.py
        model = Companies
        fields = ('name', 'address', 'contacts', 'logo', 'info', 'owner', 'id')

class CompaniesDetailSerializer(serializers.ModelSerializer):
    
    is_favorite=serializers.SerializerMethodField()
    
    class Meta: #copy from forms.py
        model = Companies
        fields = ('name', 'address', 'contacts', 'logo', 'info', 'owner', 'id', 'is_favorite')

    
    def get_is_favorite(self, obj):
        user = self.context.get('user')
        favorite = CompaniesFavorite.objects.filter(user=user, company=obj)
        if favorite:
            return True
        else:
            return False
    
        

class CompaniesCreateSerializer(serializers.ModelSerializer):
    class Meta: #copy from forms.py
        model = Companies
        fields = ('name', 'address', 'contacts', 'logo', 'info')

    def create(self, validated_data):
        owner = self.context.get('owner')
        company = Companies.objects.create(owner=owner, **validated_data)
        company.save()
        return company

class CompaniesEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('name', 'address', 'logo', 'contacts', 'info')



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('company','title', 'text', 'logo', 'id')

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta: #copy from forms.py
        model = Post
        fields = ('company','title', 'text', 'logo')

    
class PostEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text', 'logo')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('company','post', 'text','created_date','logo', 'id')

class CommentsCreateSerializer(serializers.ModelSerializer):
    class Meta: #copy from forms.py
        model = Comments
        fields = ('company','post', 'text', 'logo')
        
class CommentsEditSerializer(serializers.ModelSerializer):
    class Meta: #copy from forms.py
        model = Comments
        fields = ('text', 'logo')