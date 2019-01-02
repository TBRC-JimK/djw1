from django.contrib import admin

<<<<<<< Updated upstream
from .models import Contributor, Item, Volume, Submittal, Test
=======
# External classes here!
from applib.models import Contributor, Item, Volume, Submittal, Test
>>>>>>> Stashed changes


# Register your models here, so they appear in the admin site
admin.site.register(Item)
admin.site.register(Contributor)
admin.site.register(Volume)
admin.site.register(Submittal)
admin.site.register(Test)
