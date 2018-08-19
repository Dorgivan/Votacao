from django.contrib import admin

from .models import User, Suggestion, Comment, Vote

admin.site.register(User)
admin.site.register(Suggestion)
admin.site.register(Comment)
admin.site.register(Vote)
# Register your models here.
