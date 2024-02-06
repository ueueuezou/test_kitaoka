from django.contrib import admin

from .models import News, Com, Comment, Link


admin.site.register(News)
admin.site.register(Com)
admin.site.register(Comment)
admin.site.register(Link)