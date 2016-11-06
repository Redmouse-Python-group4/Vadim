from django.contrib import admin

from .models import Comments
# Register your models here.


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'pub_date', 'enable')
    list_filter = ['article', 'author', 'pub_date', 'enable']
    search_fields = ['article']

admin.site.register(Comments, CommentsAdmin)
