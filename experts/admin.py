from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Type, Sphere, Sex, Structure, Experts, Organization, Country
# Register your models here.


@admin.register(Experts)
class ExpertsAdmin(admin.ModelAdmin):
    list_display = ("id", "fname", "name", "type", "sphere", "country", "get_image")
    list_display_links = ("fname", "name", "type", "get_image")
    list_filter = ("type", "sphere", "sex")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="auto"')

    get_image.short_description = "Изображение"


admin.site.register(Type)
admin.site.register(Sphere)
admin.site.register(Sex)
admin.site.register(Structure)
admin.site.register(Organization)
admin.site.register(Country)
