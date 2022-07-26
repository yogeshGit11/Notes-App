from django.contrib import admin
from .models import mynotes

# Register your models here.
@admin.register(mynotes)

class notemodeladmin(admin.ModelAdmin):
    list_display=['id','topic','title','note','timedate']    