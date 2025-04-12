from django.contrib import admin

from blog.models import Blog, BlogType, Comment


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass