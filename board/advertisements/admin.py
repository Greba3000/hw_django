from django.contrib import admin
from advertisements.models import *


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementStatus)
class AdvertisementStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementType)
class AdvertisementTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementHeading)
class AdvertisementHeadingAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementAuthor)
class AdvertisementAuthorAdmin(admin.ModelAdmin):
    pass
