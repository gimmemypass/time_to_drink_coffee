from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug',  'published_date')
    list_filter = ('author', 'published_date', 'created_date')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ['published_date']
    

admin.site.register(Post, PostAdmin)
