from django.contrib import admin
from .models import Bd
from .models import Rubric

class BdAdmin(admin.ModelAdmin):
    list_display=('fact','rubric','level','content','published')
    list_display_links=('fact','level','content')
    search_fields=('fact', 'level',)
admin.site.register(Bd, BdAdmin)
admin.site.register(Rubric)


# Register your models here.
