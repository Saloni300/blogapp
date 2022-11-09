from django.contrib import admin
from apps.BlogApp.models import Blog,Comment,Category,Tag

# admin.site.register(Blog)
# admin.site.register(Comment)
# Register your models here.
class PostCategory(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_at')
    list_filter = ("status",)
    search_fields = ['title', 'detail']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Blog, PostAdmin)

admin.site.register(Category,PostCategory)
admin.site.register(Tag)

