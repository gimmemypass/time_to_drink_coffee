from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True,max_length=200, unique_for_date='published_date')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        args = [
                self.published_date.year,
                self.published_date.strftime('%m'),
                self.published_date.strftime('%d'),
                self.slug
        ]
        return reverse('blog:post_detail', args=args)
    class Meta:
        ordering = ("-published_date",)
    
    def __str__(self):
        return self.title

