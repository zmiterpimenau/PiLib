from django.contrib import admin

# Register your models here.

from . import models


admin.site.register(models.Author)
admin.site.register(models.Serie)
admin.site.register(models.Genre)
admin.site.register(models.Publisher)