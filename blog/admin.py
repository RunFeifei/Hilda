from django.contrib import admin

from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    # 后台文章管理列表的title文案
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # 新增文章时候的输入选项
    fields = ['title', 'body', 'excerpt', 'category', 'tags', 'modified_time']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
