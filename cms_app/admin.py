from django.contrib import admin
from .models import Site, Item, BusinessProcess, ProcessFile

admin.site.register(Site)
admin.site.register(Item)
admin.site.register(BusinessProcess)
admin.site.register(ProcessFile)
