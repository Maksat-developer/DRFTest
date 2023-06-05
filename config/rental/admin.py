from django.contrib import admin
from .models import Newclient, Friend, Borrowed, Belonging

admin.site.register(Newclient)
admin.site.register(Friend)
admin.site.register(Borrowed)
admin.site.register(Belonging)
