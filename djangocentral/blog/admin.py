from django.contrib import admin
from .models import Post, User, Category, Page, Comment, user_actions
# Register your models here.

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Comment)
admin.site.register(user_actions)

