from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django import forms

from firmware_uploads.models import FirmwareUpload, SEMVER_ORDER

admin.site.register(LogEntry)


class FirmwareUploadModelForm(forms.ModelForm):
    comments = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = FirmwareUpload
        exclude = ()


@admin.register(FirmwareUpload)
class FirmwareUploadAdmin(admin.ModelAdmin):
    form = FirmwareUploadModelForm
    list_display = ("__str__", "uploaded_at", "comments")
    readonly_fields = ("uploaded_at",)
    ordering = SEMVER_ORDER
