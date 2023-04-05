from django.contrib import admin
from .models import TweetModel, TweetComment

# Register your models here.
admin.site.register(TweetModel)
admin.site.register(TweetComment)