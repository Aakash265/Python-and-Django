from django.contrib import admin
from .models import Details

# Register your models here.


# Using Djnago Decorator
# @admin.register(Details) 


class Detail_Admin(admin.ModelAdmin):
    list_display = ["names", "contact", "interests"]

admin.site.register(Details, Detail_Admin)
