from django.contrib import admin
from .models import shortURL, URLClick
# Register your models here.


admin.site.register(shortURL)
admin.site.register(URLClick)

