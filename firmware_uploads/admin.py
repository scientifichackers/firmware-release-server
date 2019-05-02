import semantic_version
from django.contrib import admin
from django.contrib.admin.models import LogEntry

from firmware_uploads.models import FirmwareUpload, SEMVER_ORDER

admin.site.register(LogEntry)


def semver_sort_key(it: FirmwareUpload):
    return semantic_version.Version(it.version)


@admin.register(FirmwareUpload)
class FirmwareUploadAdmin(admin.ModelAdmin):
    list_display = ("__str__", "uploaded_at", "comments", "deferred")
    readonly_fields = ("uploaded_at",)
    ordering = SEMVER_ORDER
