from django.contrib import admin

from .models import Contributor, Item, Volume, Submittal, Test


# Register your models here, so they appear in the admin site
admin.site.register(Item)
admin.site.register(Contributor)
admin.site.register(Volume)
admin.site.register(Submittal)
admin.site.register(Test)
