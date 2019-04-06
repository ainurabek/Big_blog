from django.contrib import admin
from .models import Companies,CompaniesFavorite, Post, Comments


admin.site.register(Companies)
admin.site.register(CompaniesFavorite)
admin.site.register(Post)
admin.site.register(Comments)