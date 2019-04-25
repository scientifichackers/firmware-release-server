from rest_framework import serializers

from firmware_uploads.models import FirmwareUpload


class FirmwareUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FirmwareUpload
        fields = (
            "version",
            "firmware_bin",
            "bootloader_bin",
            "partitions_bin",
            "comments",
            "uploaded_at",
        )
