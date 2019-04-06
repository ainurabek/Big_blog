from django.conf import settings
from django.db import models
from django.utils import timezone



class Companies(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contacts = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo_folder', blank=True, null=True)
    info = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name='Company' #когда заходишь на админку он будет во множествомб желательно на русском
        verbose_name_plural = 'Companies'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #чтобы название возвращало то, что мы даем, иначе он будет возвращать object(1), object(2)
        return self.name

class CompaniesFavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Companies, related_name='is_favorite', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранная компания'
        verbose_name_plural = 'Избранные компании'

    def __str__(self):
        return self.company.name

class Post(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.DO_NOTHING, related_name='post_company', blank=True, null=True)
    title = models.CharField(max_length=200) #vezde verbose_name nado dobavlyat
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    logo = models.ImageField(upload_to='post_folder')
    

    class Meta:
        verbose_name='Post'
        verbose_name_plural = 'Posts'

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comments(models.Model):
    company=models.ForeignKey(Companies, on_delete=models.DO_NOTHING, related_name='comments_company', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, related_name='post', blank=True, null=True)
    text = models.TextField()
    logo = models.ImageField(upload_to='comments_folder')
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)


    class Meta:
        verbose_name='Comment'
        verbose_name_plural = 'Comments'

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
